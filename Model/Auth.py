import os

import requests
from dotenv import load_dotenv
from requests import Response

load_dotenv()


class Auth:
    @classmethod
    def login(cls, account=None) -> Response:
        if account is None:
            account = {}
        else:
            keys = list(dict(account))
            if 'email' not in keys or 'password' not in keys:
                print("account", account, "does not contain 'email' and 'password' in keys")
                account = {}
        url = os.getenv('API_URL')
        return requests.post(f"{url}/login", json=account, headers={
            "content-type": "Application/json"
        })

    @classmethod
    def logout(cls, token) -> Response:
        url = os.getenv('API_URL')
        return requests.post(f"{url}/logout", headers={
            "content-type": "Application/json",
            "Authorization": f"Bearer {token}"
        })
