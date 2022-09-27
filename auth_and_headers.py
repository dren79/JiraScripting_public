import requests
from dotenv import load_dotenv
import os

load_dotenv()


def auth_and_headers():
    auth = requests.auth.HTTPBasicAuth(os.environ.get("JIRA_EMAIL"), os.environ.get("API_KEY"))

    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json"
    }

    url = os.environ.get("BASE_URL")

    return auth, headers, url


def gc_client_secret():
    client = os.environ.get("GC_CLIENT")
    secret = os.environ.get("GC_SECRET")

    return client, secret