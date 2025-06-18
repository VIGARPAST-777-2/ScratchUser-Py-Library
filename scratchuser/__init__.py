import requests
import json

BASE_URL = "https://api.scratch.mit.edu/users"

class ScratchUser:
    def __init__(self, username):
        self.username = username
        self.data = self._fetch_user_data()

    def _fetch_user_data(self):
        url = f"{BASE_URL}/{self.username}"
        res = requests.get(url)
        if res.status_code != 200:
            raise ValueError(f"Usuario '{self.username}' no encontrado.")
        return res.json()

    # ----------------
    # Información base
    # ----------------
    def get_id(self):
        return self.data.get("id")

    def get_username(self):
        return self.data.get("username")

    def is_scratch_team(self):
        return self.data.get("scratchteam", False)

    def get_joined_date(self):
        return self.data.get("history", {}).get("joined")

    def get_profile_id(self):
        return self.data.get("profile", {}).get("id")

    def get_bio(self):
        return self.data.get("profile", {}).get("bio", "")

    def get_status(self):
        return self.data.get("profile", {}).get("status", "")

    def get_country(self):
        return self.data.get("profile", {}).get("country", "")

    def get_images(self):
        return self.data.get("profile", {}).get("images", {})

    def get_all_info(self):
        return {
            "id": self.get_id(),
            "username": self.get_username(),
            "profile_id": self.get_profile_id(),
            "scratchteam": self.is_scratch_team(),
            "joined": self.get_joined_date(),
            "bio": self.get_bio(),
            "status": self.get_status(),
            "country": self.get_country(),
            "images": self.get_images()
        }

    # ------------------------
    # Funciones extra (nuevas)
    # ------------------------

    def get_projects(self, limit=20, offset=0):
        url = f"{BASE_URL}/{self.username}/projects?limit={limit}&offset={offset}"
        res = requests.get(url)
        if res.status_code == 200:
            return res.json()
        return []

    def get_followers(self, limit=40, offset=0):
        url = f"{BASE_URL}/{self.username}/followers?limit={limit}&offset={offset}"
        res = requests.get(url)
        if res.status_code == 200:
            return res.json()
        return []

    def get_following(self, limit=40, offset=0):
        url = f"{BASE_URL}/{self.username}/following?limit={limit}&offset={offset}"
        res = requests.get(url)
        if res.status_code == 200:
            return res.json()
        return []

    def save_all_info_json(self, filename="user_info.json"):
        with open(filename, "w", encoding="utf-8") as f:
            json.dump(self.get_all_info(), f, indent=2, ensure_ascii=False)
