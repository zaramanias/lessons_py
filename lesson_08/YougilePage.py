import requests

base_url = "https://yougile.com/api-v2"


class YougileApi:
    def __init__(self):
        self.token = None
        self.headers = {}

    def login(self, login, password, company_id):
        resp = requests.post(f"{base_url}/auth/keys/get", json={
            "login": login, "password": password, "companyId": company_id})
        self.token = resp.json()[0]["key"]
        self.headers = {"Authorization": f"Bearer {self.token}"}
        return resp

    def get_proj(self, proj_id=None):
        if proj_id:
            url = f"{base_url}/projects/{proj_id}"
        else:
            url = f"{base_url}/projects"
        resp = requests.get(url, headers=self.headers)
        return resp

    def new_proj(self, title, user_id):
        resp = requests.post(f"{base_url}/projects", json={
            "title": title, "users": {user_id: "admin"}}, headers=self.headers)
        return resp

    def edit_proj(self, proj_id, deleted=None):
        resp = requests.put(f"{base_url}/projects/{proj_id}", json={
            "deleted": deleted}, headers=self.headers)
        return resp
