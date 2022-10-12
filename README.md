# JiraScripting

This repo is being made available as is, minimal tidy-up has been done, I will continue to support and refactor as time allows.

This is code I have used to create hundreds of Jira tickets in minutes saving hours/days of Jira Donkey work.

Refactors, updates, additions and new ways of using this would be greatly appreciated, please consider contributing. 

### What is this repository for? ###

* Quick summary - Automating Jira Epic / Story creation
* Version - working beta


### How do I get set up? ###
* Normal Python 3.10 setup should be followed.
* A virtual environment should be set up `python3 -m venv .`
* Install the imported packages `pip3 install -r requirements.txt`
* Create a copy of the .env_template file with the name .env
* Fill out the necessary fields in the newly created .env file
* Your API token can be created by: 
  1. logging into Jira
  2. Click on your avatar in the top right
  3. Click Account Settings
  4. Navigate to the Security tab on the left
  5. Click Create and manage API tokens
* If creating stories from a CSV file, place it in the inputs folder to avoid sensitive data being committed to the repo.
* If creating an output file (Json files are outputted by some scripts), please put it in the outputs folder to avoid sensitive data being committed to the repo.


* At present this is a collection of scripts that can be used independently or combined to accomplish more complex Jira tasks. 
* Some files committed to the repo are designed to accomplish specific goals and can serve as an example of how the different files can be combined.
* The aws_emailer directory . 

### Fair Warning ###
The pdf production file required some additional work to get working.
For me `pip install wkhtmltopdf`  worked.

### Contribution guidelines ###

* Please contribute frequently and openly #oneGenesys

### Who do I talk to? ###

* Original Creator - David Renton david.renton@genesys.com
* Great resource, code reviewer and sounding board - Kevin Sanderson (SecDev) kevin.sanderson@genesys.com
