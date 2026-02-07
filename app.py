import streamlit as st
import pandas as pd
from datetime import date, timedelta
from mock_data import generate_mock_data
from engine import ChaserEngine
from models import Status

st.set_page_config(
    page_title="Advisory AI - Agentic Chaser Dashboard",
    layout="wide"
)
st.markdown("""
<style>
    .main {
        background-color: #f8f9fa;
    }
    .stMetric {
        background-color: #ffffff;
        padding: 15px;
        border-radius: 10px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.05);
    }
    .status-stuck {
        color: #dc3545;
        font-weight: bold;
    }
    .status-pending {
        color: #ffc107;
        font-weight: bold;
    }
    .status-sent {
        color: #0d6efd;
        font-weight: bold;
    }
</style>
""", unsafe_allow_html=True)

st.title("Agentic Chaser Dashboard")
st.markdown("Automating operational follow ups for financial and legal advisory firms.")

if 'simulation_results' not in st.session_state:
    st.session_state.simulation_results = None

with st.sidebar:
    st.header("Simulation Settings")
    days_to_simulate = st.slider("Days to simulate", 1, 60, 20)
    if st.button(" Run Simulation", use_container_width=True):
        clients, providers, cases = generate_mock_data()
        engine = ChaserEngine(clients, providers)
        
        start_date = date.today()
        daily_snapshots = []
        all_actions = []
        
        for day in range(days_to_simulate):
            current_date = start_date + timedelta(days=day)
            engine.process_cases(cases, current_date)
            
            # Record actions
            for action in engine.actions_taken:
                all_actions.append({"date": current_date, "action": action})
            
            # Record state snapshot (simplified)
            case_data = []
            for case in cases:
                for loa in case.loas:
                    case_data.append({
                        "Case": case.title,
                        "Type": "LOA",
                        "Entity": engine.providers[loa.provider_id].name,
                        "Status": loa.status,
                        "Chases": loa.chases_count
                    })
                for doc in case.doc_requests:
                    case_data.append({
                        "Case": case.title,
                        "Type": "Doc Request",
                        "Entity": doc.doc_type,
                        "Status": doc.status,
                        "Chases": doc.chases_count
                    })
            daily_snapshots.append({"date": current_date, "data": case_data})
        
        st.session_state.simulation_results = {
            "snapshots": daily_snapshots,
            "actions": all_actions,
            "final_cases": cases,
            "engine": engine
        }

# Main Content
if st.session_state.simulation_results:
    results = st.session_state.simulation_results
    
    # Metrics
    col1, col2, col3 = st.columns(3)
    total_actions = len(results['actions'])
    final_snapshot = results['snapshots'][-1]['data']
    stuck_items = len([i for i in final_snapshot if i['Status'] == Status.STUCK])
    
    with col1:
        st.metric("Total Agent Actions", total_actions)
    with col2:
        st.metric("Active Chases", len(final_snapshot))
    with col3:
        st.metric("Stuck Issues", stuck_items, delta_color="inverse")

    # Detailed Views
    tab1, tab2 = st.tabs([" Current Case Load", " Agent Activity Log"])
    
    with tab1:
        st.header("Current Operational Status")
        df = pd.DataFrame(final_snapshot)
        st.dataframe(df, use_container_width=True)

    with tab2:
        st.header("Agent Decision History")
        if results['actions']:
            actions_df = pd.DataFrame(results['actions'])
            st.table(actions_df)
        else:
            st.info("No actions required during this simulation period.")

else:
    st.info("👈 Use the sidebar to configure and run the simulation.")
    
    # Overview Feature Cards
    col_feat1, col_feat2, col_feat3 = st.columns(3)
    with col_feat1:
        st.subheader("Autonomous Chasing")
        st.write("Identifies delays in client or provider responses and triggers follow-ups automatically.")
    with col_feat2:
        st.subheader("Multi-Channel Support")
        st.write("Respects client preferences (Email, WhatsApp, SMS) and handles provider phone calls.")
    with col_feat3:
        st.subheader("Stuck Detection")
        st.write("Flags cases where traditional follow-ups fail, alerting human supervisors to intervene.")
