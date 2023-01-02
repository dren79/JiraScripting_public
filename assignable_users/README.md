# JiraScripting - Assignable Users

A single file as this is the answer to one of the most asked Jira Cloud Automation questions on StackOverflow.

### What is in this section? ###

* One file, two methods:
  * Get all assignable users ID and UserName
  * Get all assignable users ID and email (preferred)
* Return - Json object, either UserName: ID, or Email: ID
* Email: ID is preferred, although it requires accounts to have their visibility set to `Anyone` this is accessed under - Manage Profile - Profile and Visibility under 
Contact, set to 'Anyone'.
If your instance in a corporate managed one, this is set on your behalf. Should this not be set to Anyone, the alternative UserName: ID method s provided.