class AuthService:
    def __init__(self, client, settings):
        self.client = client
        self.settings = settings

    def login(self):
        payload = {
            "username": self.settings["auth"]["username"],
            "password": self.settings["auth"]["password"],
            "expiresInMins": 30
        }
        resp = self.client.post(self.settings["auth"]["login_endpoint"], json=payload)
        resp.raise_for_status()
        return resp.json()["accessToken"]
