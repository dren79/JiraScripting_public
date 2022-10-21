from assignable_users.get_assignable_users import get_all_assignable_users_email
import json

from create_jira_tickets.create_jira_issue import create_issue
from helpers import get_all_projects, get_single_project

all_projects = get_all_projects()

for project in all_projects:
    project_key = project.get('key', None)
    project = get_single_project(project_key)
    project_lead_id = project.get('lead', {}).get('accountId', "-1")
    project_lead_display_name = project.get('lead', {}).get('displayName', "No Name Attached")
    created_issue = create_issue(
        summary=f"I am a test in project {project_key}"
        , project=project_key
        , description="This is a test, please delete me."
        , issue_type="Story"
        , assignee_id=project_lead_id
        , priority='High'
    )

    json_res = json.loads(created_issue.text)
    story_key = json_res.get('key', None)
    print(f"Newly created Story - Key: {story_key} Assigned to: {project_lead_id} ({project_lead_display_name})")

