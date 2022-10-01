import requests
import json
from auth_and_headers import jira_auth_and_headers


def create_issue(summary, project, description, epic_link=None, assignee_id=None, components=None, priority="3", issue_type="Story"):
    """Creates a story under an epic

      Parameters:
          summary (string): The issue summary.
          project (string): Project key eg. SECCOMPPM.
          description (string): The issue description.
          epic_link (string): The epic identifier eg: SECCOMPPM-93.
          assignee_id (string): The ID of the assignable user.
          components (string): The component ID is mandatory on some boards where one project satisfies multiple services.
          issue_type (string): Text description of what entity you wish to create eg, Story, Bug, Task
          priority(string): Text Highest, High, Medium, Low, Lowest

      Returns:
        response object: This will have the response code and in the text will have the details of the created issue.

     """
    auth, headers, base_url = jira_auth_and_headers()
    # create content
    content_list = []
    paragraph_content = []
    content_obj = {}
    content = {'text': description, 'type': "text"}
    content_obj['type'] = "paragraph"
    paragraph_content.append(content)
    content_obj['content'] = paragraph_content

    # create issue
    issue = {'fields': {}}
    issue['fields']['summary'] = summary
    issue['fields']['issuetype'] = {'name': issue_type}
    issue['fields']['project'] = {'key': project}
    content_list.append(content_obj)
    issue['fields']['description'] = {'type': "doc", 'version': 1, 'content': content_list}
    issue['fields']['priority'] = {'name': priority}
    if assignee_id is not None:

        issue['fields']['assignee'] = {'id': assignee_id}
    else:
        issue['fields']['assignee'] = {'id': "-1"}

    if epic_link is not None:
        issue['fields']['customfield_10300'] = epic_link
    if components is not None:
        issue['fields']['components'] = [{'id': components}]

    url = f"{base_url}/rest/api/3/issue"

    payload = json.dumps(issue)

    response = requests.request(
       "POST",
       url,
       data=payload,
       headers=headers,
       auth=auth
    )
    return response


if __name__ == "__main__":
    res = create_issue(
        summary="Delete Me"
        , project="D1"
        , description="This is a test, please delete me."
        , issue_type="Story"
        # , epic_link="SECCOMPPM-6"
        , assignee_id="david renton"
        , priority='High'
        # , components="30075"
        )
    if res.status_code == 400:
        json_res = json.loads(res.text)
        print(json_res['errors'])
    else:
        json_res = json.loads(res.text)
        story_id = json_res['id']
        story_key = json_res['key']
        print(f"ID: {story_id}, Key: {story_key} ")