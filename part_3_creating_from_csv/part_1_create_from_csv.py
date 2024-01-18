import csv
import json

from src import create_issue


def main(file_):
    with open(file_) as infile:
        reader = csv.reader(infile, delimiter=",")
        # Skip the header
        next(reader, None)
        # For each row
        for row in reader:
            res = create_issue(
                summary=f"From CSV - {row[1]} {row[2]}"
                , project="D2"
                , description=f"""
This could be used to assign people : {row[3]}
Gender : {row[4]}
ip : {row[5]}
Message : {row[6]}"""
                , issue_type="Story"
                , epic_link="D2-2"
                , assignee_id="557058:e747a920-b560-47ee-82e3-94ffe7a59a1b"
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
    input_file = "input/MOCK_DATA.csv"
    main(input_file)