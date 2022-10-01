import requests
from auth_and_headers import jira_auth_and_headers
import json

def get_issue(issue_key):
    auth, headers, base_url = jira_auth_and_headers()
    url = f"{base_url}/rest/api/3/issue/{issue_key}"

    response = requests.request(
        "GET",
        url,
        headers=headers,
        auth=auth
    )
    text_contents = json.loads(response.text)
    return text_contents


def get_issue_types():
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


def get_all_projects():
    projects = []
    auth, headers, base_url = jira_auth_and_headers()
    url = f"{base_url}/rest/api/3/project/search"

    while url is not None:
        response = requests.request(
            "GET",
            url,
            headers=headers,
            auth=auth
        )
        json_res = json.loads(response.text)
        current_list_of_projects = json_res.get('values')
        for proj in current_list_of_projects:
            projects.append(proj)
        url = json_res.get("nextPage", None)

    return projects


def get_all_issue_link_types():
    auth, headers, base_url = jira_auth_and_headers()
    url = f"{base_url}/rest/api/3/issueLinkType"

    response = requests.request(
        "GET",
        url,
        headers=headers,
        auth=auth
    )
    json_res = json.loads(response.text)
    issue_link_types = json_res.get('issueLinkTypes')

    return issue_link_types


def get_emails_from_issue(this_issue_id):
    auth, headers, base_url = jira_auth_and_headers()
    url = f"{base_url}/rest/api/3/issue/{this_issue_id}"
    people = {}
    response = requests.request(
        "GET",
        url,
        headers=headers,
        auth=auth
    )

    json_res = json.loads(response.text)
    assignee_email = json_res['fields'].get('assignee', {}).get('emailAddress', "No Email listed")
    assignee_name = json_res['fields'].get('assignee', {}).get('displayName', "No Name listed")
    this_assignee = {"assignee_name": assignee_name, "assignee_email": assignee_email}
    people['assignee'] = this_assignee

    reporter_email = json_res['fields'].get('reporter', {}).get('emailAddress', "No Email listed")
    reporter_name = json_res['fields'].get('reporter', {}).get('displayName', "No Name listed")
    this_reporter = {"reporter_name": reporter_name, "reporter_email": reporter_email}
    people['reporter'] = this_reporter
    people['issue_key'] = this_issue_id

    return people


def get_stories_from_epic(epic):
    """Gets all stories attached to an epic

    Parameters:
        epic (string): Epic identifier eg: SECCOMPPM-93
    Returns:
        Json Object: Key is story key, attributes: status_name, status_category, priority_name, project_name and project_key

   """
    epic_name = epic
    startAt = 0
    stories_in_epic = {}
    auth, headers, base_url = jira_auth_and_headers()
    url = f"{base_url}/rest/agile/1.0/epic/{epic_name}/issue?maxResults=50&startAt={startAt}"
    while url is not None:
        response = requests.request(
            "GET",
            url,
            headers=headers,
            auth=auth
        )
        ret_json = json.loads(response.text)
        total_expected_results = ret_json.get('total', 0)
        for issue in ret_json["issues"]:
            issue_key = issue.get("key", None)
            stories_in_epic[f'{issue_key}'] = {}
            stories_in_epic[f'{issue_key}']["status_name"] = issue.get('fields', {}).get('status', {}).get('name', None)
            stories_in_epic[f'{issue_key}']["status_category"] = issue.get('fields', {}).get('status', {}).get('statusCategory', {}).get('key', None)
            stories_in_epic[f'{issue_key}']["project_key"] = issue.get('fields', {}).get('project', {}).get('key', None)
            stories_in_epic[f'{issue_key}']["project_name"] = issue.get('fields', {}).get('project', {}).get('name', None)
            stories_in_epic[f'{issue_key}']["priority_name"] = issue.get('fields', {}).get('priority', {}).get('name', None)
        if len(stories_in_epic) != total_expected_results:
            startAt = startAt + 50
            url = f"{base_url}/rest/agile/1.0/epic/{epic_name}/issue?maxResults=50&startAt={startAt}"
        else:
            url = None

    return stories_in_epic


if __name__ == "__main__":
    issue_key = "D1-7"
    issue = get_issue(issue_key)
    print(json.dumps(issue, indent=4))

    # issue_types = get_issue_types()
    # print(json.dumps(issue_types, indent=4))

    # priorities = get_priority_types()
    # print(json.dumps(priorities, indent=4))

    # projects = get_all_projects()
    # print(json.dumps(projects, indent=4))

    # issue_links = get_all_issue_link_types()
    # print(json.dumps(issue_links, indent=4))

    # get_emails = get_emails_from_issue('D1-5')
    # print(json.dumps(get_emails, indent=4))

    # epic_name = "D1-7"
    # issues_in_epic = get_stories_from_epic(epic_name)
    # print(json.dumps(issues_in_epic, indent=4))