import json

from src import create_epic


def main():
    res = create_epic(
        summary="This is a summary",
        project="D2",
        description="This is a description for an epic",
        epic_name="Some Epic Name",
        priority="High",
        assignee_id='-1')
    json_res = json.loads(res.text)
    story_key = json_res['key']
    print(f"New Epic created - Key: {story_key} ")


if __name__ == "__main__":
    main()
