import requests
from auth_and_headers import jira_auth_and_headers
import json

from helpers import get_issue_types, get_priority_types, get_all_epic_link_types


def main():
    my_instance = {}
    issue_types = get_issue_types()
    my_instance['issue_types'] = []
    for issue_type in issue_types:
        my_instance['issue_types'].append(issue_type.get('name', None))

    priorities = get_priority_types()
    my_instance['priorities'] = []
    for priority_ in priorities:
        my_instance['priorities'].append(priority_.get('name', None))

    issue_links = get_all_epic_link_types()
    my_instance['issue_links'] = []
    for issue_link in issue_links:
        my_instance['issue_links'].append(issue_link.get('name', None))

    return my_instance


if __name__ == "__main__":
    my_instance_details = main()
    with open(f'my_jira_cloud_instance/my_instance_details.json', 'w') as outfile:
        json.dump(my_instance_details, outfile)