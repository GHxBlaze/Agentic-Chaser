# Agentic Chaser

Agentic Chaser prototype in Python designed to lessen the administrative burden on Financial Advisors.

---
## Case Management and Agentic Chaser Implementation Plan

The objective is to build an Agentic Chaser that automates the admininstrative burden of chasing Letters of Authority (LOA) and client documents for Financial Advisors.

### Proposed Changes

#### models.py

- `Client`: Basic information and preferences.
- `Provider`: Pension/Investment provider details.
- `LOA`: Linked to Client and Provider, tracks current state (Sent, Signed, Received by Provider, Complete).
- `DocumentRequest`: Specific documents needed from clientlike passport, payslip etc.
- `Case`: Groups LOAs and Document Requests for a specific client goal, e.g. pension consolidation.

#### engine.py 

- `ChaserEnginer`: Evaluates the state of all active items.
- Logic to determine "Chasing Rules" (e.g., if Provider LOA is > 10 days old, escalate).
- Decisions on communication channels based on urgency and previous responses.

#### mock_data.py

- Generators for realistic client scenarios.
- Time series simulation

#### main.py

- CLI or simple web dashboard (FastAPI/Streamlit) to interact with the system.
- Logs showing the "Agent" in action sneding chasers.

### Verification Plan

#### Automated Tests

- Unit tests for state transition logic.
- Validation that the chaser triggers correctly at specific time intervals.

### Manual Verification

- Execute the simulation and observe the console output/dashboard to ensure that Agentic behavior feels authetic to the advisor's needs.

#### Core Logic and models


## Key Features

- **State Driven Logic**: The system tracks the exact status of every Letter of Authority (LOA) and Document Request.
-  **Agentic Decision Engine**: Automatically decides when to chase a client via their preferred channel like Email, Whatsapp, SMS etc, or when to flag a provider as stuck after excessive delays.
-  **Python 3.4 Compatibility**: Refactored to run on legacy environments while maintaining clean object oriented design.

---

## Components

- **models.py**: Core entities(Client, Provider, Case, LOA).
- **engine.py**: The intelligence layer that evaluates dates and triggers actions.
- **mock_data.py**: Realistic advisor scenarios including pension consolidation and onboarding.
- **main.py**: The dashboard simulation.

---

## Simulation Results

The simulation successfully demostrated:

### 1.) **Client Chasing**
Daily checks and identify clients who haven't signed LOAs or provided documents.
### 2.) **Provider Monitoring**
Tracking response times against provider averages and escalating when items are overdue.
### 3.) **Escalation**
Markings items as "STUCK" when they fall outside normal processing windows.

```bash
# To run the simulation:
python main.py
```
### Example Dashboard Output

```bash
CASE: Pension Consolidation (Client ID: c1)
------------------------------
  LOAs:
    - Aviva           [Pending]    Chases: 5
    - Royal London    [Pending]    Chases: 5
  Document Requests:
    - Passport        [Pending]     Chases: 3

--- AGENT ACTIONS TODAY ---
 > CHASE CLIENT: Sent Email to John Doe regarding 'LOA for Aviva' (Chase #5)
 > CHASE PROVIDER: Called Royal London regarding John Doe's LOA (Wait time approx 30m)
```

