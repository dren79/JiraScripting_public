import csv
import hashlib
import json
import os
from datetime import datetime

from assignable_users.get_assignable_users import get_all_assignable_users_email
from create_jira_tickets.create_fancy_jira_issue import create_issue
from emailer.aws_emailer.email_with_attachment import send_mail
from part_4_creating_assigning_and_emailing._description_document import description_doc
from part_4_creating_assigning_and_emailing._email_body import email_body

assignable_users = get_all_assignable_users_email('D1')


def main(file_, epic_, initiative_name_):
    init_ = {}
    f_name = f"reports/{initiative_name_}.json"
    if os.path.exists(f_name):
        with open(f'reports/{initiative_name_}.json', 'r+') as initiative_:
            init_ = json.load(initiative_)
    else:
        init_['created'] = []
        init_['stories'] = {}
    with open(file_) as infile:
        reader = csv.reader(infile, delimiter=",")
        # Skip the header
        next(reader, None)
        # For each row
        for row in reader:
            row_tuple = tuple(row)
            hash_ = hashlib.md5()
            for entry in row_tuple:
                hash_.update(entry.encode())
            row_hash = hash_.hexdigest()
            # Are we doing work or not?
            if row_hash not in init_['created']:
                # get user id from email, this could be provided in th csv file
                date_ = datetime.now()
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
                try:
                    res = create_issue(
                        summary=f"From CSV - {first_name} {last_name}"
                        , project=project
                        , description_doc=description_document
                        , issue_type="Story"
                        , epic_link=epic_
                        , assignee_id=assignable_user_id
                        , priority='High'
                    )
                    json_res = json.loads(res.text)
                    story_key = json_res['key']
                    init_['stories'][f'{story_key}'] = {
                        "date_opened": f"{date_}",
                        "assignee": f"{assignable_user_email}",
                        "assignee_id": f"{assignable_user_id}",
                        "hash": f"{row_hash}",
                        "status_category": "new",
                        "reminder": []
                    }
                    init_['created'].append(row_hash)
                except Exception as e:
                    with open(f'reports/{initiative_name_}.json', 'w') as outfile:
                        json.dump(init_, outfile)
                    print(f"Exception: {e} \nFor: {row}")

                sender_ = 'david.renton@genesys.com'
                recipients_ = [f'{assignable_user_email}']
                cc_ = ['davidleerenton@gmail.com', 'hello@devfestireland.com']
                title_ = 'DevFest Ireland'
                text_ = 'DevFest is awesome'
                body_ = email_body(first_name, last_name, gender, ip_address, message, project, story_key)
                attachments_ = ['input/devfestireland_with_image.png']
                try:
                    response_ = send_mail(sender_, recipients_, cc_, title_, text_, body_, attachments_)
                    print(response_)
                    init_['stories'][f'{story_key}']['reminder'].append(f"Email with subject {title_} was sent to {recipients_} on {date_}")
                except:
                    with open(f'reports/{initiative_name_}.json', 'w') as outfile:
                        json.dump(init_, outfile)
        with open(f'reports/{initiative_name_}.json', 'w') as outfile:
            json.dump(init_, outfile)


if __name__ == "__main__":
    initiative_name = "go_to_devfest"
    input_file = "input/MOCK_DATA_WITH_PROJECT_3_lines.csv"
    epic = "D2-2"
    main(input_file, epic, initiative_name)

    with open(f'reports/{initiative_name}.json', 'r+') as initiative:
        init = json.load(initiative)
    print(json.dumps(init, indent=4))

    # Some stories got added
    ready_to_add_some_more = input("Ready to add more stories?")
    initiative_name = "go_to_devfest"
    input_file = "input/MOCK_DATA_WITH_PROJECT_6_lines.csv"
    main(input_file, epic, initiative_name)

    ready_to_see_the_result_2 = input("press any key")
    with open(f'reports/{initiative_name}.json', 'r+') as initiative:
        init = json.load(initiative)
    print(json.dumps(init, indent=4))
