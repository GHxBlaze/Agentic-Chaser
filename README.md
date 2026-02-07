# Advisory AI - Agentic Chaser

**Advisory AI** is an autonomous "Chaser" engine designed for financial and legal advisory firms. It automates the tedious process of operational follow-ups, ensuring that Pensions, Letters of Authority (LOA), and client document requests never fall through the cracks.

## Problem & Solution

### The Chosen Problem
In financial advisory, consultants spend hours manually chasing providers (like Aviva or Royal London) and clients for signatures and documents. Delays in these operational steps slow down the entire advice process, leading to poor client outcomes and lost revenue.

### Our Solution: The Agentic Chaser
Advisory AI acts as an autonomous operations assistant. It:
1. **Monitors Wait Times**: Tracks exactly how long a provider or client has had a pending request.
2. **Triggers Intelligent Chases**: Automatically sends follow-ups via the client's preferred channel (Email, WhatsApp, or SMS).
3. **Escalates Issues**: If a provider doesn't respond within their average wait time, the agent "calls" (simulated) the provider. If it remains unresolved, it's flagged as **STUCK** for human intervention.

---

## Tech Stack
- **Python 3.10+**: Core logic and engine.
- **Streamlit**: Interactive dashboard for simulation and visualization.
- **Pandas**: Data handling and reporting.

---

## Local Setup

### Prerequisites
- Python installed on your machine.
- `pip` (Python package manager).

### Installation
1. Clone the repository:
   ```bash
   git clone <your-repo-url>
   cd anti
   ```
2. Install dependencies:
   ```bash
   pip install streamlit pandas
   ```

### Running the Project
To launch the interactive dashboard:
```bash
streamlit run app.py
```

---

## Project Structure
- `app.py`: The Streamlit web interface.
- `engine.py`: Core logic for the Agentic Chaser.
- `models.py`: Data structures for Clients, Providers, and Cases.
- `mock_data.py`: Simulated advisory environment.
- `main.py`: CLI version of the simulation.
  
## Hosted Application
The application is live and accessible at:  
**https://agentic-chaser-lnis6i8nhs3ggjcewa9nu2.streamlit.app/**


---




