# JiraScripting

This repo is being made available as is, minimal tidy-up has been done, I will continue to support and refactor as time allows (pull requests welcome).

This is code I have used to create hundreds of Jira tickets in minutes saving hours/days of Jira Donkey work.

Refactors, updates, additions and new ways of using this would be greatly appreciated, please consider contributing. 

## What is this repository for? ##

* Quick summary:
  * Automating Jira Epic & Story creation
  * Commenting on issues
  * Emailing assignees
  * Tracking actions performed for easy follow up

### Usecases ###

* Audit request list (SOC2, C5, PCI DSS)
* Gap analysis output (Any security gap list from any consultancy)
* CVE check (Verify non-existence, not vulnerable or updated across many teams with report as evidence)
* Quarterly security check output that needs to be remediated
* Multi project upgrade work (e.g. all services need to upgrade encryption to TLS 1.3 or FIPS 140-3)
* Output work from Datadog or Sumo Logic


## How do I get set up? ##
* Normal Python 3.10 setup should be followed.
  * A virtual environment should be set up `python3 -m venv .`
  * Activate the virtual environment `source venv/Workspace/projects/bin/activate` (this may be different on your system)
  * Install the imported packages `pip3 install -r requirements.txt` (this may be different on your system)
* Set up a free instance of Jira Cloud `https://www.atlassian.com/software/jira/free`
* Create a copy of the .env_template file and name it `.env` exactly
* Fill out the necessary fields in the newly created .env file
* Your API token can be created by: 
  1. logging into Jira Cloud (the one you created earlier)
  2. Click on your avatar in the top right
  3. Click Account Settings
  4. Navigate to the Security tab on the left
  5. Click Create and manage API tokens
* If creating stories from a CSV file, place it in the inputs folder to avoid sensitive data being committed to the repo.
* If creating a report output file (Json files are outputted by some scripts), please put it in the reports folder to avoid sensitive data being committed to the repo.


## I'm set up, what's next? ##
* The repository is set up in folders bringing the user from the basic operations through to the more complete solutions. Part 0 through to part 4.
* Some functionality is offered in its own folder for easy transplanting into the learner's project for example assignable_users and emailer.
* The just_for_fun folder is a collection of code used for pairing a presentation on this repository so is offered here as it may help someone down the line.



* At present this is a collection of scripts that can be used independently or combined to accomplish more complex Jira tasks. 
* Some files committed to the repo are designed to accomplish specific goals and can serve as an example of how the different files can be combined.
* To use the aws_emailer or GCP emailer an active account with separate credentials is needed. 


### Contribution guidelines ###

* Please contribute frequently and openly!

### Who do I talk to? ###

* Original Creator - David Renton david.renton@genesys.com
