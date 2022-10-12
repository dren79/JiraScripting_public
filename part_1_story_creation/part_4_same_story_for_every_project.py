from assignable_users.get_assignable_users import get_all_assignable_users_email
import json

from create_jira_tickets.create_jira_issue import create_issue
from just_for_fun.HTML.json_to_html import json_to_html_page
from helpers import get_all_projects

all_projects = get_all_projects()
assignable_users = get_all_assignable_users_email('D1')

campaign_report = {}

for project in all_projects:
    campaign_report[f"{project.get('key', None)}"] = {}

for project_key in campaign_report:
    if project_key is not None:
        created_issue = create_issue(
            summary=f"I am a test in project {project_key}"
            , project=project_key
            , description="This is a test, please delete me."
            , issue_type="Story"
            , assignee_id=assignable_users.get('davidleerenton@gmail.com', None)
            , priority='High'
        )

        json_res = json.loads(created_issue.text)
        story_key = json_res.get('key', None)
        campaign_report[f'{project_key}']['created_story'] = story_key

campaign_name = "my_super_report"
with open(f'reports/{campaign_name}_report.json', 'w') as outfile:
    json.dump(campaign_report, outfile)

html_page = json_to_html_page(campaign_report)
file = open(f'reports/{campaign_name}_report.html', 'w')
file.write(html_page)
file.close()