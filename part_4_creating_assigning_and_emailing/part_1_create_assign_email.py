import csv
import json

from assignable_users.get_assignable_users import get_all_assignable_users_email
from create_jira_tickets.create_fancy_jira_issue import create_issue
from emailer.aws_emailer.email_with_attachment import send_mail
from part_4_creating_assigning_and_emailing._description_document import description_doc
from part_4_creating_assigning_and_emailing._email_body import email_body

assignable_users = get_all_assignable_users_email('D1')


def main(file_):
    with open(file_) as infile:
        reader = csv.reader(infile, delimiter=",")
        # Skip the header
        next(reader, None)
        # For each row
        for row in reader:
            # get user id from email, this could be provided in th csv file
            assignable_user_email = 'davidleerenton@gmail.com'
            assignable_user_id = assignable_users.get(assignable_user_email, None)
            # these don't need to be assigned, this way just makes it more readable when debugging.
            first_name = row[1]
            last_name = row[2]
            email = row[3]
            gender = row[4]
            ip_address = row[5]
            message = row[6]
            project = row[7]
            # Create the description document
            description_document = description_doc(first_name, last_name, email, gender, ip_address, message)
            # Build and execute the call to the Jira Cloud API
            res = create_issue(
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
                story_key = json_res['key']
                print(f"Story created - Key: {story_key} ")

            sender_ = 'david.renton@genesys.com'
            recipients_ = [f'{assignable_user_email}']
            cc_ = ['davidleerenton@gmail.com', 'hello@devfestireland.com']
            title_ = 'DevFest Ireland'
            text_ = 'DevFest is awesome'
            body_ = email_body(first_name, last_name, gender, ip_address, message, project, story_key)
            attachments_ = ['input/devfestireland_with_image.png']

            response_ = send_mail(sender_, recipients_, cc_, title_, text_, body_, attachments_)
            print(response_)


if __name__ == "__main__":
    input_file = "input/MOCK_DATA_WITH_PROJECT.csv"
    main(input_file)
