import json

from create_jira_tickets.create_jira_epic import create_epic
from helpers import create_epic_link


def main():
    epic_names = ["Epic one", "Epic two", "Epic three", "Dave", "Other Dave", "Big Dave",
                  "Tommy Dave", "Jana Dave", "Rich Dave", "Patrick Paterson"]

    uber_epic_creation = create_epic(
        summary="This is a summary",
        project="D2",
        description="This is a description for an uber epic",
        epic_name="One Epic to rule them all",
        priority="High",
        assignee_id='-1')
    json_res = json.loads(uber_epic_creation.text)
    uber_epic_key = json_res['key']

    for epic_name in epic_names:
        epic_creation = create_epic(
            summary="This is a summary",
            project="D3",
            description="This is a description for an uber epic",
            epic_name=epic_name,
            priority="High",
            assignee_id='-1')
        json_res = json.loads(epic_creation.text)
        epic_key = json_res['key']

        link_response = create_epic_link(epic_key, uber_epic_key, 'Relates')
        print(link_response)


if __name__ == "__main__":
    main()