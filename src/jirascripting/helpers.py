
import requests
from src.jirascripting.auth_and_headers import jira_auth_and_headers
import json


def get_issue(this_issue_key):
    """Gets all fields for the epic or story queried

        Parameters:
            this_issue_key (string): issue identifier eg: D1-1
        Returns:
            Json Object: Object has all fields available set and vacant for the story/epic

   """
    auth, headers, base_url = jira_auth_and_headers()
    url = f"{base_url}/rest/api/3/issue/{this_issue_key}"

    response = requests.request(
        "GET",
        url,
        headers=headers,
        auth=auth
    )
    text_contents = json.loads(response.text)
    return text_contents


def get_servicedesk_issue(this_issue_key):
    """Gets all fields for the epic or story queried

        Parameters:
            this_issue_key (string): issue identifier eg: D1-1
        Returns:
            Json Object: Object has all fields available set and vacant for the story/epic

   """
    auth, headers, base_url = jira_auth_and_headers()
    url = f"{base_url}/rest/servicedeskapi/request/{this_issue_key}"

    response = requests.request(
        "GET",
        url,
        headers=headers,
        auth=auth
    )
    text_contents = json.loads(response.text)
    return text_contents


def get_issue_status_category(this_issue_key):
    """Gets all fields for the epic or story queried and returns the status category

        Parameters:
            this_issue_key (string): issue identifier eg: D1-1
        Returns:
            String: status category new, indeterminate or done

   """
    auth, headers, base_url = jira_auth_and_headers()
    url = f"{base_url}/rest/api/3/issue/{this_issue_key}"

    response = requests.request(
        "GET",
        url,
        headers=headers,
        auth=auth
    )
    issue_json = json.loads(response.text)
    status_category = issue_json.get('fields', {}).get('status', {}).get('statusCategory', {}).get('key', None)
    return status_category


def get_issue_status(this_issue_key):
    """Gets all fields for the epic or story queried and returns the status category

        Parameters:
            this_issue_key (string): issue identifier eg: D1-1
        Returns:
            String: status category new, indeterminate or done

   """
    auth, headers, base_url = jira_auth_and_headers()
    url = f"{base_url}/rest/api/3/issue/{this_issue_key}"

    response = requests.request(
        "GET",
        url,
        headers=headers,
        auth=auth
    )
    issue_json = json.loads(response.text)
    status_ = issue_json.get('fields', {}).get('status', {}).get('name', None)
    return status_


def get_single_project(this_project_id):
    """Gets all fields set and vacant for the epic or story queried

       Parameters:
           this_project_id (string): project identifier eg: D1
       Returns:
           Json Object: Object has all project information

    """
    auth, headers, base_url = jira_auth_and_headers()

    # single project
    url = f"{base_url}/rest/api/3/project/{this_project_id}"

    response = requests.request(
        "GET",
        url,
        headers=headers,
        auth=auth
    )
    json_res = json.loads(response.text)
    return json_res


def get_all_projects():
    """Gets all projects in this jira instance, will return archived projects also

       Returns:
           Json Object: describes the projects n this jira instance

    """
    projects_ = []
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
            projects_.append(proj)
        url = json_res.get("nextPage", None)

    return projects_


def create_epic_link(link_from, link_to, link_type):
    """Links epics together in a number of meaningful ways
        Parameters:
            link_from (string): epic key eg: D1-1 this is the new epic, the child
            link_to (string): epic key eg: D1-1 this is the uber epic, the parent
            link_type (string): Relates, Blocks, Cloners, Duplicate
        Returns:
           Json Object:

    """
    auth, headers, base_url = jira_auth_and_headers()
    url = f"{base_url}/rest/api/3/issueLink"

    payload = json.dumps({
        "outwardIssue": {
            "key": f"{link_from}"
        },
        "inwardIssue": {
            "key": f"{link_to}"
        },
        "type": {
            "name": f"{link_type}"
        }
    })

    response = requests.request(
        "POST",
        url,
        data=payload,
        headers=headers,
        auth=auth
    )
    text_response = "No link created"
    if response.ok:
        text_response = f"{link_from} now {link_type} {link_to}"
    return text_response


def get_issue_assignee(this_issue_id):
    """Gets all stories attached to an epic

        Parameters:
            this_issue_id (string): issue identifier eg: D1-1
        Returns:
            Json Object: Object has assignee_name, assignee_email, reporter_name, reporter_email

   """
    auth, headers, base_url = jira_auth_and_headers()
    url = f"{base_url}/rest/api/3/issue/{this_issue_id}"
    response = requests.request(
        "GET",
        url,
        headers=headers,
        auth=auth
    )

    json_res = json.loads(response.text)
    assignee_email = json_res['fields'].get('assignee', {}).get('emailAddress', None)
    assignee_name = json_res['fields'].get('assignee', {}).get('displayName', None)
    assignee_id = json_res['fields'].get('assignee', {}).get('accountId', None)
    this_assignee = {"assignee_name": assignee_name, "assignee_email": assignee_email, "assignee_id": assignee_id}

    return this_assignee


def get_stories_from_epic(epic):
    """Gets all stories attached to an epic

    Parameters: epic (string): Epic identifier eg: SECCOMPPM-93 Returns: Json Object: Key is story key, attributes:
    status_name, status_category, priority_name, project_name and project_key

   """
    epic_name = epic
    start_at = 0
    stories_in_epic = {}
    auth, headers, base_url = jira_auth_and_headers()
    url = f"{base_url}/rest/agile/1.0/epic/{epic_name}/issue?maxResults=50&start_at={start_at}"
    while url is not None:
        response = requests.request(
            "GET",
            url,
            headers=headers,
            auth=auth
        )
        ret_json = json.loads(response.text)
        total_expected_results = ret_json.get('total', 0)
        for this_issue in ret_json["issues"]:
            this_issue_key = this_issue.get("key", None)
            stories_in_epic[f'{this_issue_key}'] = {}
            stories_in_epic[f'{this_issue_key}']["status_name"] = this_issue.get(
                'fields', {}).get('status', {}).get('name', None)
            stories_in_epic[f'{this_issue_key}']["status_category"] = this_issue.get(
                'fields', {}).get('status', {}).get('statusCategory', {}).get('key', None)
            stories_in_epic[f'{this_issue_key}']["project_key"] = this_issue.get(
                'fields', {}).get('project', {}).get('key', None)
            stories_in_epic[f'{this_issue_key}']["project_name"] = this_issue.get(
                'fields', {}).get('project', {}).get('name', None)
            stories_in_epic[f'{this_issue_key}']["priority_name"] = this_issue.get(
                'fields', {}).get('priority', {}).get('name', None)
        if len(stories_in_epic) != total_expected_results:
            start_at = start_at + 50
            url = f"{base_url}/rest/agile/1.0/epic/{epic_name}/issue?maxResults=50&start_at={start_at}"
        else:
            url = None

    return stories_in_epic


def add_comment_to_story(this_issue_key, comment):
    auth, headers, base_url = jira_auth_and_headers()
    url = f"{base_url}/rest/api/3/issue/{this_issue_key}/comment"
    comment_template = {'body': {}}
    comment_template['body']['type'] = "doc"
    comment_template['body']['version'] = 1
    comment_template['body']['content'] = []
    content_parent = {"type": "paragraph", "content": []}
    content_child = {"text": f"{comment}", "type": "text"}
    content_parent['content'].append(content_child)
    comment_template['body']['content'].append(content_parent)

    payload = json.dumps(comment_template)

    response = requests.request(
        "POST",
        url,
        data=payload,
        headers=headers,
        auth=auth
    )
    return response


def add_fancy_comment_to_story(this_issue_key, comment_doc):
    auth, headers, base_url = jira_auth_and_headers()
    url = f"{base_url}/rest/api/3/issue/{this_issue_key}/comment"
    comment_template = {'body': comment_doc}
    payload = json.dumps(comment_template)

    response = requests.request(
        "POST",
        url,
        data=payload,
        headers=headers,
        auth=auth
    )
    return response


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


def get_transitions(issue_key_):
    """Gets all link types in this jira instance

       Returns:
           Json Object: describes the available epic linking adjectives

    """
    auth, headers, base_url = jira_auth_and_headers()
    url = f"{base_url}/rest/api/3/issue/{issue_key_}/transitions"

    response = requests.request(
        "GET",
        url,
        headers=headers,
        auth=auth
    )
    json_res = json.loads(response.text)
    # epic_link_types = json_res.get('issueLinkTypes')

    return json_res


def get_comments(issue_key_):
    """Gets all comments in this issue

          Returns:
              Json Object: returns all comments in json in Jira document format

       """
    auth, headers, base_url = jira_auth_and_headers()
    url = f"{base_url}/rest/api/3/issue/{issue_key_}/comment"

    response = requests.request(
        "GET",
        url,
        headers=headers,
        auth=auth
    )
    json_res = json.loads(response.text)

    return json_res


def transition_issue(issue_key_, stage_id):
    """Transition issue to defined state
        Parameters:
            issue_key_ (string): issue identifier eg: D1-1
            stage_id (string): The integer id of the desired state of the issue (may be gathered from get_transitions)
        Returns:
            String: Response code, eg. 204

       """
    auth, headers, base_url = jira_auth_and_headers()
    url = f"{base_url}/rest/api/3/issue/{issue_key_}/transitions"
    payload = json.dumps({
        "transition": {
            "id": f"{stage_id}"
        },
    })
    response = requests.request(
        "POST",
        url,
        data=payload,
        headers=headers,
        auth=auth
    )
    status = response.status_code

    return f"response: {status}"


def get_all_request_types(s_desk_issue_key):
    """Gets all comments in this issue

              Returns:
                  Json Object: returns all comments in json in Jira document format

           """
    auth, headers, base_url = jira_auth_and_headers()
    url = f"{base_url}rest/servicedeskapi/requesttype"

    response = requests.request(
        "GET",
        url,
        headers=headers,
        auth=auth
    )
    json_res = json.loads(response.text)
    # epic_link_types = json_res.get('issueLinkTypes')

    return json_res


if __name__ == "__main__":
    issue_key = "DR-49"
    issue = get_issue(issue_key)
    print(json.dumps(issue, indent=4))

    project_key = "D1"
    project = get_single_project(project_key)
    print(json.dumps(project, indent=4))

    projects = get_all_projects()
    print(json.dumps(projects, indent=4))

    # First epic key is the new one you create, the second id the one you are linking to
    # The third input is the type of link - get_issue_link_types.py is in the repo
    link_res = create_epic_link("D1-7", "D1-23", "Relates")
    print(link_res)

    get_emails = get_issue_assignee('D1-5')
    print(json.dumps(get_emails, indent=4))

    epic_name = "D1-7"
    issues_in_epic = get_stories_from_epic(epic_name)
    print(json.dumps(issues_in_epic, indent=4))

    story_id = "D1-7"
    comment_text = "I made it"
    res = add_comment_to_story(story_id, comment_text)
    print(res)

    story_id = "D1-7"
    # Build fancy comments in the same way as fancy descriptions here -
    # https://developer.atlassian.com/cloud/jira/platform/apis/document/playground/
    fancy_comment_doc = {
        "version": 1,
        "type": "doc",
        "content": [
            {
                "type": "paragraph",
                "content": [
                    {
                        "type": "text",
                        "text": "this is "
                    }
                ]
            },
            {
                "type": "paragraph",
                "content": [
                    {
                        "type": "text",
                        "text": "some text"
                    }
                ]
            },
            {
                "type": "paragraph",
                "content": [
                    {
                        "type": "text",
                        "text": "and I will tag someone "
                    },
                    {
                        "type": "mention",
                        "attrs": {
                            "id": "557058:e747a920-b560-47ee-82e3-94ffe7a59a1b",
                            "text": "@DR",
                            "accessLevel": ""
                        }
                    },
                    {
                        "type": "text",
                        "text": " "
                    }
                ]
            }
        ]
    }
    res = add_fancy_comment_to_story(story_id, fancy_comment_doc)
    print(res)

    issue_types = get_issue_types()
    print(json.dumps(issue_types, indent=4))

    priorities = get_priority_types()
    print(json.dumps(priorities, indent=4))

    issue_links = get_all_epic_link_types()
    print(json.dumps(issue_links, indent=4))

    comments_in_issue = get_comments(story_id)
    print(json.dumps(comments_in_issue, indent=4))

    transitions = get_transitions(issue_key)
    print(json.dumps(transitions, indent=4))

    transition_this_issue = transition_issue(issue_key, "31")
    print(transition_this_issue)

    story_id = "D1-7"
    issue_status_category = get_issue_status_category(story_id)

    story_id = "D1-7"
    issue_status = get_issue_status(story_id)
