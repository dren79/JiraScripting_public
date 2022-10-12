import requests
from dotenv import load_dotenv
import os

load_dotenv()


def jira_auth_and_headers():
    """Gets all fields set and vacant for the epic or story queried

       Returns:
           auth: (HTTPBasicAuth object) for the Jira Cloud instance
           headers: (json object) contains required headers for all requests
           url: (String) the base URL for the instance

    """
    auth = requests.auth.HTTPBasicAuth(os.environ.get("JIRA_EMAIL_DR"), os.environ.get("API_KEY_DR"))

    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json"
    }

    url = os.environ.get("BASE_URL_DR")

    return auth, headers, url
