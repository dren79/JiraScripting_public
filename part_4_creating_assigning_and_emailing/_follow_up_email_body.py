

def email_body(story_key, status, reminders):
    body_html = f"""
<html>
    <head></head>
    <body>
        <h2>Hey;</h2>
        <br>
        <p>You have a Jira ticket still in {status}</p> <br> 
        <p><b>❤️❤️I know you are all super busy, but this needs to be done! ❤️❤️</b></p>  
        <p>You should have gotten previous reminders</p>
        <pre>
            <code>
            {reminders}
            </code>
        </pre>
        <p>Here is the Jira story we created for you to report progress - https://YOUR_PROJECT.atlassian.net/browse/{story_key}</p>
        <a href="https://YOUR_PROJECT.atlassian.net/browse/{story_key}">Here is the Jira story we created for you to report progress.</a>
    </body>
</html>"""
    return body_html