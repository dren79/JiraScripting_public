import json
from datetime import datetime

from helpers import get_issue_status, get_issue_status_category, get_issue_assignee
from part_4_creating_assigning_and_emailing._follow_up_email_body import email_body
from emailer.aws_emailer.email_with_attachment import send_mail


def main(initiative_name_):
    date_ = datetime.now()
    f_name = f"reports/{initiative_name_}.json"
    with open(f'{f_name}', 'r+') as initiative_:
        init_ = json.load(initiative_)

    for story in init_["stories"]:
        if init_["stories"][f"{story}"]["status_category"] != "done":
            story_status_category = get_issue_status_category(story)
            if story_status_category == "done":
                init_["stories"][f"{story}"]["status_category"] = story_status_category
                continue
            else:
                story_status = get_issue_status(story)
                this_assignee = get_issue_assignee(story)
                if this_assignee["assignee_id"] != init_["stories"][f"{story}"]["assignee_id"]:
                    init_["stories"][f"{story}"]["assignee_id"] = this_assignee["assignee_id"]
                    init_["stories"][f"{story}"]["assignee"] = this_assignee["assignee_email"]

                sender_ = 'david.renton@genesys.com'
                recipients_ = [f'{init_["stories"][f"{story}"]["assignee"]}']
                cc_ = ['davidleerenton@gmail.com', 'hello@devfestireland.com']
                title_ = 'DevFest Ireland'
                text_ = 'REMINDER - DevFest is awesome'
                body_ = email_body(story, story_status, init_["stories"][f"{story}"]["reminder"])
                attachments_ = ['input/devfestireland_with_image.png']
                try:
                    response_ = send_mail(sender_, recipients_, cc_, title_, text_, body_, attachments_)
                    print(response_)
                    init_['stories'][f'{story}']['reminder'].append(
                        f"Reminder email with subject {title_} was sent to {recipients_} on {date_}")
                except:
                    with open(f'reports/{initiative_name_}.json', 'w') as outfile:
                        json.dump(init_, outfile)
    with open(f'reports/{initiative_name_}.json', 'w') as outfile:
        json.dump(init_, outfile)


if __name__ == "__main__":
    initiative_name = "go_to_devfest"
    main(initiative_name)

    with open(f'reports/{initiative_name}.json', 'r+') as initiative:
        init = json.load(initiative)
    print(json.dumps(init, indent=4))
