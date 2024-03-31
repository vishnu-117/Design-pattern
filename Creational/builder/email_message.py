class EmailMessage:

    def __init__(self):
        self._from = ''
        self._to = []
        self._cc = []
        self._bcc = []
        self._subject = ''
        self._body = ''
        self._attachements = []

    def set_from(self, from_address: str):
        self._from = from_address
    
    def set_subject(self, subject: str):
        self._subject = subject
    
    def set_body(self, body: str):
        self._body = body
    
    def get_to(self):
        return self._to

    def get_cc(self):
        return self._cc
    
    def get_bbc(self):
        return self._bcc
    
    def get_attachment(self):
        return self._attachements
    
    def send(self):
        print("Email successfuly sent....")
        print(f"------------------------")
        print(f"From: {self._from}")
        print(f"To: {self._to}")
        print(f"CC: {self._cc}")
        print(f"BCC: {self._bcc}")
        print(f"Subject: {self._subject}")
        print(f"Body: {self._body}")
        print(f"Attachments: {self._attachements}")
