import json

from create_jira_tickets.create_jira_epic import create_epic

res = create_epic(
    summary="This is a summary",
    project="D2",
    description="This is a description for an epic",
    epic_name="Some Epic Name",
    priority="High",
    assignee_id='-1')
json_res = json.loads(res.text)
story_key = json_res['key']
print(f"New Epic created - Key: {story_key} ")