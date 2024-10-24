from base64 import b64encode

class Config:
    auth_string = ''

    def __init__(self, data) -> None:
        self.auth_string = b64encode(data['DEVOPS_PAT'].encode())

    def get(self, key):
        if key in self:
            return self.key
        else:
            return ''