import json
from datetime import datetime

from helpers import get_issue_status, get_issue_status_category, add_fancy_comment_to_story, get_issue_assignee
from part_4_creating_assigning_and_emailing._comment_document import comment_doc


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
                comment_document = comment_doc(init_["stories"][f"{story}"]["assignee_id"],
                                               init_["stories"][f"{story}"]["reminder"],
                                               story_status)
                try:
                    comment = add_fancy_comment_to_story(story, comment_document)
                    init_['stories'][f'{story}']['reminder'].append(
                        f"Reminder comment was added on {date_}")
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
