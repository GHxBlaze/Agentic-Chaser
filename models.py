from datetime import datetime, date

class Status:
    PENDING = "Pending"
    SENT = "Sent"
    RESEVED = "Received"
    SIGNED = "Signed"
    RETURNED = "Returned"
    COMPLETE = "Complete"
    STUCK = "Stuck"
    CHASING = "Chasing"

class CommunicationType:
    EMAIL = "Email"
    SMS = "SMS"
    PHONE = "Phone"
    WHATSAPP = "WhatsApp"

class Provider:
    def __init__(self, id, name, avg_response_days=15):
        self.id = id
        self.name = name
        self.avg_response_days = avg_response_days

class Client:
    def __init__(self, id, name, email, phone, preferred_channel=CommunicationType.EMAIL):
        self.id = id
        self.name = name
        self.email = email
        self.phone = phone
        self.preferred_channel = preferred_channel

class LOA:
    def __init__(self, id, client_id, provider_id, created_at, last_action_at, status=Status.PENDING):
        self.id = id
        self.client_id = client_id
        self.provider_id = provider_id
        self.status = status
        self.created_at = created_at
        self.last_action_at = last_action_at
        self.signed_at = None
        self.sent_to_provider_at = None
        self.chases_count = 0
        self.history = []

    def log(self, message):
        self.history.append("{}: {}".format(date.today(), message))

class DocumentRequest:
    def __init__(self, id, client_id, doc_type, requested_at, status=Status.PENDING):
        self.id = id
        self.client_id = client_id
        self.doc_type = doc_type
        self.status = status
        self.requested_at = requested_at
        self.last_chase_at = None
        self.chases_count = 0
        self.history = []

    def log(self, message):
        self.history.append("{}: {}".format(date.today(), message))

class Case:
    def __init__(self, id, client_id, title, status=Status.PENDING):
        self.id = id
        self.client_id = client_id
        self.title = title
        self.loas = []
        self.doc_requests = []
        self.status = status
