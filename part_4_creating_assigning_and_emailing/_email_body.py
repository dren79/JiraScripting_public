

def email_body(first_name, last_name, gender, ip_address, message, project, story_key):
    body_html = f"""
<html>
    <head></head>
    <body>
        <h2>Hey {first_name} {last_name};</h2>
        <br>
        <p>We have created a ticket for your attention in the Jira project {project} as a part of the super important 
        project</p> <br> <p><b>❤️❤️I know you are all super busy, but we need your help! ❤️❤️</b></p> 
        <p>{message} needs to be actioned.</p> 
        <p>This is turning out well.</p>
        <pre>
            <code>
            This is some code snippet 
            </code>
        </pre>
        <p>Add a list if it is needed?</p>
        <ul>
          <li>Gender: {gender}</li>
          <li>IP Address: {ip_address}</li>
          <li>Project: {project}</li>
        </ul>
        <p>Here is a link to the project confluence page - if there is a chance of questions, start a Confluence page for updates</p>
        <p>Here is the Jira story we created for you to report progress - https://YOUR_PROJECT.atlassian.net/browse/{story_key}</p>
        <a href="https://YOUR_PROJECT.atlassian.net/browse/{story_key}">Here is the Jira story we created for you to report progress.</a>
    </body>
</html>"""
    return body_html