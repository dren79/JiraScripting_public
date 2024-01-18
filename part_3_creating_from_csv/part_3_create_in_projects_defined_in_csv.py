import csv
import json

from src import get_all_assignable_users_email
from src import create_fancy_issue
from part_3_creating_from_csv._description_document import description_doc

assignable_users = get_all_assignable_users_email('D1')


def main(file_):
    with open(file_) as infile:
        reader = csv.reader(infile, delimiter=",")
        # Skip the header
        next(reader, None)
        # For each row
        for row in reader:
            # get user id from email, this could be provided in th csv file
            # replace the below email with one from your jira instance
            assignable_user_email = 'davidleerenton@gmail.com'
            assignable_user_id = assignable_users.get(assignable_user_email, None)

            first_name = row[1]
            last_name = row[2]
            email = row[3]
            gender = row[4]
            ip_address = row[5]
            message = row[6]
            project = row[7]
            # Create the description document
            description_document = description_doc(first_name, last_name, email, gender, ip_address, message)
            res = create_fancy_issue(
                summary=f"From CSV - {first_name} {last_name}"
                , project=project
                , description_doc=description_document
                , issue_type="Story"
                , epic_link="D2-2"
                , assignee_id=assignable_user_id
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


if __name__ == "__main__":
    input_file = "input/MOCK_DATA_WITH_PROJECT.csv"
    main(input_file)
