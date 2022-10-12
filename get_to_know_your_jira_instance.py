import requests
from auth_and_headers import jira_auth_and_headers
import json


def get_issue_types():
    """Gets all issue types in this jira instance

       Returns:
           Json Object: describes the available issue types

    """
    auth, headers, base_url = jira_auth_and_headers()
    url = f"{base_url}/rest/api/3/issuetype"

    response = requests.request(
        "GET",
        url,
        headers=headers,
        auth=auth
    )
    text_contents = json.loads(response.text)
    return text_contents


def get_priority_types():
    """Gets all priority types in this jira instance

       Returns:
           Json Object: describes the available priority types

    """
    auth, headers, base_url = jira_auth_and_headers()
    url = f"{base_url}/rest/api/3/priority"

    response = requests.request(
        "GET",
        url,
        headers=headers,
        auth=auth
    )
    text_contents = json.loads(response.text)
    return text_contents


def get_all_epic_link_types():
    """Gets all link types in this jira instance

       Returns:
           Json Object: describes the available epic linking adjectives

    """
    auth, headers, base_url = jira_auth_and_headers()
    url = f"{base_url}/rest/api/3/issueLinkType"

    response = requests.request(
        "GET",
        url,
        headers=headers,
        auth=auth
    )
    json_res = json.loads(response.text)
    epic_link_types = json_res.get('issueLinkTypes')

    return epic_link_types


if __name__ == "__main__":
    # issue_types = get_issue_types()
    # print(json.dumps(issue_types, indent=4))
    #
    # priorities = get_priority_types()
    # print(json.dumps(priorities, indent=4))

    issue_links = get_all_epic_link_types()
    print(json.dumps(issue_links, indent=4))
