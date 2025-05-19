import re

class EmailAddressParser:
    def __init__(self, addresses):
        self.addresses = addresses

    def parse(self):
        parts = re.split(r'[,\s]+', self.addresses.strip())
        valid_emails = [email for email in parts if re.fullmatch(r'\b[\w\.-]+@[\w\.-]+\.\w+\b', email)]
        return sorted(set(valid_emails))