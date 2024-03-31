from email_message import EmailMessage

class EmailBuilder:

    def __init__(self):
        self._email = EmailMessage()

    def add_from(self, from_address: str):
        self._email.set_from(from_address)
        return self
    
    def add_to(self, to: str):
        self._email.get_to().append(to)
        return self
    
    def add_cc(self, cc: str):
        self._email.get_cc().append(cc)
        return self
    
    def add_bcc(self, bcc: str):
        self._email.get_bbc().append(bcc)
        return self
    
    def with_body(self, body: str):
        self._email.set_body(body)
        return self
    
    def add_attachment(self, attachment: str):
        self._email.get_attachment().append(attachment)
        return self
    
    def with_subject(self, subject: str):
        self._email.set_subject(subject)
        return self
    
    def build(self):
        return self._email

    
