from src import get_all_assignable_users_email
import json

from src import create_issue
from src import get_all_projects


def main():
    all_projects = get_all_projects()
    assignable_users = get_all_assignable_users_email('D1')
    # replace user_email with one you have in your jira instance
    user_email = 'davidleerenton@gmail.com'
    user_id = assignable_users.get(user_email, None)

    for project in all_projects:
        project_key = project.get('key', None)
        created_issue = create_issue(
            summary=f"I am a test in project {project_key}"
            , project=project_key
            , description="This is a test, please delete me."
            , issue_type="Story"
            , assignee_id=user_id
            , priority='High'
        )

        json_res = json.loads(created_issue.text)
        story_key = json_res.get('key', None)
        print(f"Newly created Story - Key: {story_key} Assigned to: {user_id} ({user_email})")


if __name__ == "__main__":
    main()