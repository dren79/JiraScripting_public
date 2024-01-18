import atexit
import json

from src import create_epic
from src import create_epic_link
from just_for_fun.HTML.json_to_html import json_to_html_page

campaign_report = {}


def main():
    epic_names = ["Epic one", "Epic two", "Epic three"]

    uber_epic_creation = create_epic(
        summary="This is a summary",
        project="D2",
        description="This is a description for an uber epic",
        epic_name="One Epic to rule them all",
        priority="High",
        assignee_id='-1')
    json_res = json.loads(uber_epic_creation.text)
    uber_epic_key = json_res['key']
    campaign_report['uber_epic'] = {f'{uber_epic_key}': {}}
    campaign_report[f'epics'] = {}

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
        campaign_report['epics'][f'{epic_key}'] = {}

        link_response = create_epic_link(epic_key, uber_epic_key, 'Relates')
        print(link_response)


@atexit.register
def final_function():
    campaign_name = "my_super_at_exit"
    with open(f'reports/{campaign_name}_report.json', 'w') as outfile:
        json.dump(campaign_report, outfile)

    html_page = json_to_html_page(campaign_report)
    file = open(f'reports/{campaign_name}_report.html', 'w')
    file.write(html_page)
    file.close()


if __name__ == "__main__":
    main()
