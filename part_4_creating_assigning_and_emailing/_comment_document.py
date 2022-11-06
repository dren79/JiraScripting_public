# This file is imported by the part_3_create_in_projects_defined_in_csv.py and part_2_create_fancy_from_csv.py files
# The json object assigned to fancy_description is generated from - https://developer.atlassian.com/cloud/jira/platform/apis/document/playground/

def comment_doc(id_, reminder, status):
    fancy_description = {
      "version": 1,
      "type": "doc",
      "content": [
        {
          "type": "paragraph",
          "content": [
            {
              "type": "text",
              "text": "Hey "
            },
            {
              "type": "mention",
              "attrs": {
                "id": f"{id_}"
              }
            },
            {
              "type": "text",
              "text": " have you booked your ticket to DevFest yet?"
            }
          ]
        },
        {
          "type": "paragraph",
          "content": [
            {
              "type": "text",
              "text": f"This ticket was created {reminder}"
            }
          ]
        },
        {
          "type": "paragraph",
          "content": [
            {
              "type": "text",
              "text": f"It’s still in status {status}"
            }
          ]
        }
      ]
    }
    return fancy_description
