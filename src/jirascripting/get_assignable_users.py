import requests
from src.jirascripting.auth_and_headers import jira_auth_and_headers
import json


def _get_assignable_users(key, start_from):
    auth, headers, base_url = jira_auth_and_headers()
    url = f"{base_url}/rest/api/3/user/assignable/search"

    query = {
        'project': key,
        'startAt': start_from
    }

    response = requests.request(
        "GET",
        url,
        headers=headers,
        params=query,
        auth=auth
    )
    return response


def get_all_assignable_users_name(project_key):
    """Returns a Json object with usernames mapped to logical ID
          Parameters:
              project_key (string): The key of an active project in the target Jira instance.
          Returns:
            response object: Json object with available users in the targeted Jira instance with their logical ID's.
    """
    start_at = 0
    my_json = {}
    while start_at is not None:
        user_list_response = _get_assignable_users(project_key, start_at)
        text_contents = json.loads(user_list_response.text)
        for user in text_contents:
            my_json[f"{user.get('displayName', None)}"] = user.get('accountId', None)
        if len(text_contents) == 100:
            start_at = start_at + 100
        else:
            start_at = None

    return my_json


def get_all_assignable_users_email(project_key):
    """Returns a Json object with email mapped to logical ID
          Parameters:
              project_key (string): The key of an active project in the target Jira instance.
          Returns:
            response object: Json object with available users in the targeted Jira instance with their logical ID's.
    """
    start_at = 0
    my_json = {}
    while start_at is not None:
        user_list_response = _get_assignable_users(project_key, start_at)
        text_contents = json.loads(user_list_response.text)
        for user in text_contents:
            my_json[f"{user.get('emailAddress', None)}"] = user.get('accountId', None)
        if len(text_contents) == 100:
            start_at = start_at + 100
        else:
            start_at = None

    return my_json


if __name__ == "__main__":
    jira_project_key = 'D1'
    returned_json_name = get_all_assignable_users_name(jira_project_key)
    print(json.dumps(returned_json_name, indent=4))

    returned_json_email = get_all_assignable_users_email(jira_project_key)
    print(json.dumps(returned_json_email, indent=4))