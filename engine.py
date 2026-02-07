from datetime import date, timedelta
from models import Case, Client, Provider, Status, CommunicationType

class ChaserEngine:
    def __init__(self, clients, providers):
        self.clients = {c.id: c for c in clients}
        self.providers = {p.id: p for p in providers}
        self.actions_taken = []

    def process_cases(self, cases, current_date):
        self.actions_taken = []
        for case in cases:
            self._process_loas(case, current_date)
            self._process_doc_requests(case, current_date)

    def _process_loas(self, case, current_date):
        client = self.clients[case.client_id]
        for loa in case.loas:
            provider = self.providers[loa.provider_id]
            
            # Logic 1: Client hasn't signed LOA
            if loa.status == Status.PENDING:
                days_since_created = (current_date - loa.created_at).days
                if days_since_created >= 3:
                    self._chase_client(client, "LOA for {}".format(provider.name), loa)

            # Logic 2: Provider hasn't responded to sent LOA
            elif loa.status == Status.SENT:
                days_since_sent = (current_date - loa.last_action_at).days
                if days_since_sent >= provider.avg_response_days:
                    self._chase_provider(provider, client, loa)
                elif days_since_sent >= provider.avg_response_days + 10:
                    loa.status = Status.STUCK
                    loa.log("Marked as STUCK: No response from provider after {} days.".format(days_since_sent))

    def _process_doc_requests(self, case, current_date):
        client = self.clients[case.client_id]
        for doc in case.doc_requests:
            if doc.status == Status.PENDING:
                days_since_requested = (current_date - doc.requested_at).days
                
                # Chase every 5 days
                last_chase = doc.last_chase_at or doc.requested_at
                days_since_chase = (current_date - last_chase).days
                
                if days_since_chase >= 5:
                    self._chase_client(client, "Document: {}".format(doc.doc_type), doc)

    def _chase_client(self, client, item_name, item):
        channel = client.preferred_channel
        action = "CHASE CLIENT: Sent {} to {} regarding '{}' (Chase #{})".format(
            channel, client.name, item_name, item.chases_count + 1
        )
        item.chases_count += 1
        item.log(action)
        self.actions_taken.append(action)

    def _chase_provider(self, provider, client, loa):
        action = "CHASE PROVIDER: Called {} regarding {}'s LOA (Wait time approx 30m)".format(
            provider.name, client.name
        )
        loa.chases_count += 1
        loa.log(action)
        loa.last_action_at = date.today() # Simulate activity
        self.actions_taken.append(action)
