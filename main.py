from datetime import date, timedelta
from mock_data import generate_mock_data
from engine import ChaserEngine
from models import Status

def print_dashboard(current_date, cases, engine):
    print("\n" + "="*60)
    print(" ADVISORY AI - AGENTIC CHASER DASHBOARD | Date: {}".format(current_date))
    print("="*60)
    
    for case in cases:
        print("\nCASE: {} (Client ID: {})".format(case.title, case.client_id))
        print("-" * 30)
        
        # Display LOAs
        if case.loas:
            print("  LOAs:")
            for loa in case.loas:
                provider_name = engine.providers[loa.provider_id].name
                status_color = "[STUCK]" if loa.status == Status.STUCK else "[{}]".format(loa.status)
                print("    - {:<15} {:<12} Chases: {}".format(provider_name, status_color, loa.chases_count))
        
        # Display Doc Requests
        if case.doc_requests:
            print("  Document Requests:")
            for doc in case.doc_requests:
                print("    - {:<15} [{}]     Chases: {}".format(doc.doc_type, doc.status, doc.chases_count))

    if engine.actions_taken:
        print("\n--- AGENT ACTIONS TODAY ---")
        for action in engine.actions_taken:
            print(" > {}".format(action))
    else:
        print("\n--- No actions required today ---")

def run_simulation(days=15):
    clients, providers, cases = generate_mock_data()
    engine = ChaserEngine(clients, providers)
    
    start_date = date.today()
    
    for day in range(days):
        current_date = start_date + timedelta(days=day)
        
        # Run the engine
        engine.process_cases(cases, current_date)
        
        # Only print if actions were taken or it's the first/last day
        if engine.actions_taken or day == 0 or day == days - 1:
            print_dashboard(current_date, cases, engine)
            # Minimal pause if actions were taken
            if engine.actions_taken:
                pass 

if __name__ == "__main__":
    run_simulation(20)
