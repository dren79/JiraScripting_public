import requests
import json
from src import jira_auth_and_headers


def create_epic(summary, project, description, epic_name, priority, assignee_id="-1"):
    """Creates an epic

      Parameters:
          summary (string): The issue summary
          project (string): What Jira project should this be in SECCOMPPM is 21697
          description (string): The issue description
          epic_name (string): The name of this epic
          priority (string): Text Highest, High, Medium, Low, Lowest
          assignee_id (string): The ID of the assignable user.

      Returns:
        response object: this will have the response code and in the text will have the details of the created epic

     """
    auth, headers, base_url = jira_auth_and_headers()
    # create issue
    url = f"{base_url}/rest/api/3/issue"

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
    issue['fields']['issuetype'] = {'name': 'Epic'}
    issue['fields']['project'] = {'key': project}
    content_list.append(content_obj)
    issue['fields']['description'] = {'type': "doc", 'version': 1, 'content': content_list}
    issue['fields']['priority'] = {'name': priority}
    issue['fields']['assignee'] = {'id': assignee_id}
    issue['fields']['customfield_10011'] = f"{epic_name}"

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
    res = create_epic(
        summary="This is a summary",
        project="D2",
        description="This is a description for an epic",
        epic_name="Some Epic Name",
        priority="High")
    json_res = json.loads(res.text)
    story_id = json_res['id']
    story_key = json_res['key']
    print(f"ID: {story_id}, Key: {story_key} ")
