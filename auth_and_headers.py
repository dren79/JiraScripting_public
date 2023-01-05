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
    auth = requests.auth.HTTPBasicAuth(os.environ.get("JIRA_EMAIL"), os.environ.get("API_KEY"))

    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json"
    }

    url = os.environ.get("BASE_URL")

    return auth, headers, url
