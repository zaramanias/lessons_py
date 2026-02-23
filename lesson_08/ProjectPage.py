import requests

base_url = "https://yougile.com/api-v2/"


class ProjectPage:
    def __init__(self, token):
        self.headers = {"Authorization": f"Bearer{token}"}

    def get_all_proj(self):
        resp = requests.get(f"{base_url}/projects", headers=self.headers)
        return resp
