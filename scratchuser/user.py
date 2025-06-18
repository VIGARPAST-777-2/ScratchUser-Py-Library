import requests
import json

class ScratchUser:
    def __init__(self, username):
        self.username = username
        self.api_url = f"https://api.scratch.mit.edu/users/{username}"
        self.data = self._get_user_data()

    def _get_user_data(self):
        response = requests.get(self.api_url)
        if response.status_code == 200:
            return response.json()
        else:
            raise ValueError(f"Usuario '{self.username}' no encontrado.")

    def get_all_info(self):
        return self.data

    def get_username(self):
        return self.data.get("username", "")

    def get_bio(self):
        return self.data.get("profile", {}).get("bio", "")

    def get_status(self):
        return self.data.get("profile", {}).get("status", "")

    def get_country(self):
        return self.data.get("profile", {}).get("country", "")

    def get_joined_date(self):
        return self.data.get("history", {}).get("joined", "")

    def get_image(self):
        return self.data.get("profile", {}).get("images", {}).get("90x90", "")

    def get_projects(self, limit=5):
        url = f"https://api.scratch.mit.edu/users/{self.username}/projects/?limit={limit}"
        response = requests.get(url)
        return response.json() if response.status_code == 200 else []

    def get_followers(self, limit=5):
        url = f"https://api.scratch.mit.edu/users/{self.username}/followers/?limit={limit}"
        response = requests.get(url)
        return response.json() if response.status_code == 200 else []

    def get_following(self, limit=5):
        url = f"https://api.scratch.mit.edu/users/{self.username}/following/?limit={limit}"
        response = requests.get(url)
        return response.json() if response.status_code == 200 else []

    def save_all_info_json(self, filename="user_info.json"):
        with open(filename, "w", encoding="utf-8") as f:
            json.dump(self.data, f, indent=2, ensure_ascii=False)
