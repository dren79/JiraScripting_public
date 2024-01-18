import json
import requests
from src.jirascripting.auth_and_headers import jira_auth_and_headers


def create_fancy_issue(summary, project, description_doc, parent=None, assignee_id=None, priority="High", issue_type="Story"):
    """Creates an ADF(markdown) story under an epic, use the pyadf library to build out the description document
    https://developer.atlassian.com/cloud/jira/platform/apis/document/playground/

      Parameters:
          :param summary: (string) The issue summary.
          :param project: (string) Project key eg. D1-1.
          :param description_doc: (string) Use the Document Builder here https://developer.atlassian.com/cloud/jira/platform/apis/document/playground/.
          :param parent: (string): The key of the parent epic
          :param assignee_id: (string) The ID of the assignable user (use get_assignable_users to get this).
          :param issue_type: (string) Text name of the issue type you wish to create eg, Story, Bug, Task
          :param priority: (string) Text - Highest, High, Medium, Low, Lowest

      Returns:
        response object: This will have the response code and in the text will have the details of the created issue.

     """
    auth, headers, base_url = jira_auth_and_headers()

    # create issue
    issue = {'fields': {}}
    if parent is not None:
        issue['fields']['parent'] = {'key': parent}
    issue['fields']['summary'] = summary
    issue['fields']['issuetype'] = {'name': issue_type}
    issue['fields']['project'] = {'key': project}
    issue['fields']['description'] = description_doc
    issue['fields']['priority'] = {'name': priority}
    if assignee_id is not None:
        issue['fields']['assignee'] = {'id': assignee_id}
    else:
        issue['fields']['assignee'] = {'id': "-1"}

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
    formatted_description = {
        "version": 1,
        "type": "doc",
        "content": [
            {
                "type": "paragraph",
                "content": [
                    {
                        "type": "text",
                        "text": "Generated from the "
                    },
                    {
                        "type": "text",
                        "text": "Document Builder",
                        "marks": [
                            {
                                "type": "link",
                                "attrs": {
                                    "href": "https://developer.atlassian.com/cloud/jira/platform/apis/document/playground/"
                                }
                            }
                        ]
                    }
                ]
            },
            {
                "type": "paragraph",
                "content": [
                    {
                        "type": "text",
                        "text": "I am bold",
                        "marks": [
                            {
                                "type": "strong"
                            }
                        ]
                    }
                ]
            },
            {
                "type": "paragraph",
                "content": [
                    {
                        "type": "text",
                        "text": "I am itallic",
                        "marks": [
                            {
                                "type": "em"
                            }
                        ]
                    }
                ]
            },
            {
                "type": "paragraph",
                "content": [
                    {
                        "type": "text",
                        "text": "List"
                    }
                ]
            },
            {
                "type": "bulletList",
                "content": [
                    {
                        "type": "listItem",
                        "content": [
                            {
                                "type": "paragraph",
                                "content": [
                                    {
                                        "type": "text",
                                        "text": "one"
                                    }
                                ]
                            }
                        ]
                    },
                    {
                        "type": "listItem",
                        "content": [
                            {
                                "type": "paragraph",
                                "content": [
                                    {
                                        "type": "text",
                                        "text": "two"
                                    }
                                ]
                            }
                        ]
                    },
                    {
                        "type": "listItem",
                        "content": [
                            {
                                "type": "paragraph",
                                "content": [
                                    {
                                        "type": "text",
                                        "text": "three"
                                    }
                                ]
                            }
                        ]
                    }
                ]
            },
            {
                "type": "paragraph",
                "content": []
            },
            {
                "type": "codeBlock",
                "attrs": {
                    "language": "python"
                },
                "content": [
                    {
                        "type": "text",
                        "text": "def some_python_method():\n  me = some_variable\n  return me"
                    }
                ]
            }
        ]
    }
    res = create_fancy_issue(
        summary="MarkDown Test"
        , project="D1"
        , description_doc=formatted_description
        , issue_type="Story"
        # , epic_link="SECCOMPPM-6"
        , assignee_id="557058:e747a920-b560-47ee-82e3-94ffe7a59a1b"
        , priority='High'
    )
    if res.status_code == 400:
        json_res = json.loads(res.text)
        print(json_res['errors'])
    else:
        json_res = json.loads(res.text)
        story_id = json_res['id']
        story_key = json_res['key']
        print(f"ID: {story_id}, Key: {story_key} ")
