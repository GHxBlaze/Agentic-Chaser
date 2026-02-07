from datetime import date, timedelta
import random
from models import Client, Provider, LOA, DocumentRequest, Case, CommunicationType, Status

def generate_mock_data():
    providers = [
        Provider(id="p1", name="Aviva", avg_response_days=15),
        Provider(id="p2", name="Royal London", avg_response_days=20),
        Provider(id="p3", name="Standard Life", avg_response_days=12),
        Provider(id="p4", name="Prudential", avg_response_days=25)
    ]

    clients = [
        Client(id="c1", name="John Doe", email="john@example.com", phone="07123456789", preferred_channel=CommunicationType.EMAIL),
        Client(id="c2", name="Jane Smith", email="jane@example.com", phone="07987654321", preferred_channel=CommunicationType.WHATSAPP),
        Client(id="c3", name="Robert Brown", email="robert@example.com", phone="07111222333", preferred_channel=CommunicationType.SMS)
    ]

    cases = []
    
    # Case 1: Active Pension Consolidation
    case1 = Case(id="case1", client_id="c1", title="Pension Consolidation")
    case1.loas = [
        LOA(id="l1", client_id="c1", provider_id="p1", created_at=date.today() - timedelta(days=20), last_action_at=date.today() - timedelta(days=20)),
        LOA(id="l2", client_id="c1", provider_id="p2", created_at=date.today() - timedelta(days=5), last_action_at=date.today() - timedelta(days=5))
    ]
    case1.doc_requests = [
        DocumentRequest(id="d1", client_id="c1", doc_type="Passport", requested_at=date.today() - timedelta(days=10), status=Status.PENDING)
    ]
    cases.append(case1)

    # Case 2: New Client Onboarding
    case2 = Case(id="case2", client_id="c2", title="Retirement Planning")
    case2.doc_requests = [
        DocumentRequest(id="d2", client_id="c2", doc_type="Recent Payslip", requested_at=date.today() - timedelta(days=2), status=Status.PENDING),
        DocumentRequest(id="d3", client_id="c2", doc_type="P60", requested_at=date.today() - timedelta(days=2), status=Status.PENDING)
    ]
    cases.append(case2)

    return clients, providers, cases
