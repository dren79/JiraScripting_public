import requests
from dotenv import load_dotenv
import os

load_dotenv()


def jira_auth_and_headers():
    auth = requests.auth.HTTPBasicAuth(os.environ.get("JIRA_EMAIL_DR"), os.environ.get("API_KEY_DR"))

    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json"
    }

    url = os.environ.get("BASE_URL_DR")

    return auth, headers, url
