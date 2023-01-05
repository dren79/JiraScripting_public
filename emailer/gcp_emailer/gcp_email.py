import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail, Email
from python_http_client.exceptions import HTTPError


def send_mail(sender: str, recipients: list, title: str, html: str = None) -> dict:
    """
    Send email to recipients. Sends one mail to all recipients.
    To set this up on the GCP console follow this tutorial
    https://cloud.google.com/compute/docs/tutorials/sending-mail/using-sendgrid .
    """
    # If using this module handle the API key with respect
    sg = SendGridAPIClient(os.environ['EMAIL_API_KEY'])

    html_content = html

    message = Mail(
        to_emails=recipients,
        from_email=Email(sender),
        subject=title,
        html_content=html_content
        )

    try:
        response = sg.send(message)
        return_message = f"email.status_code={response.status_code}"
        #expected 202 Accepted

    except HTTPError as e:
        return_message = e.message

    return return_message


if __name__ == '__main__':
    # replace sender_ with the email address you registered in AWS SES
    sender_ = 'david.renton@genesys.com'
    recipients_ = ['davidleerenton@gmail.com']
    title_ = 'DevFest'
    text_ = 'DevFest is awesome'
    body_ = """<html><head></head><body><h1>A header 1</h1><br>Some text."""

    response_ = send_mail(sender_, recipients_, title_, text_, body_)
    print(response_)