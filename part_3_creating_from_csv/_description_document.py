# This file is imported by the part_3_create_in_projects_defined_in_csv.py and part_2_create_fancy_from_csv.py files
# The json object assigned to fancy_description is generated from - https://developer.atlassian.com/cloud/jira/platform/apis/document/playground/

def description_doc(first_name, last_name, email, gender, ip_address, message):
    fancy_description = {
      "version": 1,
      "type": "doc",
      "content": [
        {
          "type": "heading",
          "attrs": {
            "level": 1
          },
          "content": [
            {
              "type": "text",
              "text": f"Hey {first_name} {last_name} "
            },
            {
              "type": "emoji",
              "attrs": {
                "shortName": ":wave:",
                "id": "1f44b",
                "text": "👋"
              }
            },
            {
              "type": "text",
              "text": " "
            }
          ]
        },
        {
          "type": "paragraph",
          "content": [
            {
              "type": "text",
              "text": "This story description was build "
            },
            {
              "type": "text",
              "text": "here",
              "marks": [
                {
                  "type": "link",
                  "attrs": {
                    "href": "https://developer.atlassian.com/cloud/jira/platform/apis/document/playground/"
                  }
                }
              ]
            },
            {
              "type": "text",
              "text": " !"
            }
          ]
        },
        {
          "type": "paragraph",
          "content": [
            {
              "type": "text",
              "text": "Email, "
            },
            {
              "type": "text",
              "text": f"could have been used to assign the ticket {email}",
              "marks": [
                {
                  "type": "em"
                }
              ]
            },
            {
              "type": "text",
              "text": " "
            },
            {
              "type": "emoji",
              "attrs": {
                "shortName": ":man_shrugging:",
                "id": "1f937-200d-2642-fe0f",
                "text": "🤷‍♂️"
              }
            },
            {
              "type": "text",
              "text": " "
            }
          ]
        },
        {
          "type": "bulletList",
          "content": [
            {
              "type": "listItem",
              "content": [
                {
                  "type": "paragraph",
                  "content": [
                    {
                      "type": "text",
                      "text": f"Gender : {gender}"
                    }
                  ]
                }
              ]
            },
            {
              "type": "listItem",
              "content": [
                {
                  "type": "paragraph",
                  "content": [
                    {
                      "type": "text",
                      "text": f"IP : {ip_address}"
                    }
                  ]
                }
              ]
            },
            {
              "type": "listItem",
              "content": [
                {
                  "type": "paragraph",
                  "content": [
                    {
                      "type": "text",
                      "text": f"Message : {message}"
                    }
                  ]
                }
              ]
            }
          ]
        },
        {
          "type": "paragraph",
          "content": [
            {
              "type": "text",
              "text": "This is some code:"
            }
          ]
        },
        {
          "type": "codeBlock",
          "attrs": {
            "language": "python"
          },
          "content": [
            {
              "type": "text",
              "text": "res = create_issue(\n    summary=f\"From CSV - {first_name} {last_name}\"\n    , project=\"D2\"\n    , description_doc=description_document\n    , issue_type=\"Story\"\n    , epic_link=\"D2-2\"\n    , assignee_id=assignable_user_id\n    , priority='High'\n)"
            }
          ]
        },
        {
          "type": "paragraph",
          "content": []
        }
      ]
    }

    return fancy_description
