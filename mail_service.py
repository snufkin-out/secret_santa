# https://mailtrap.io/blog/python-send-email-gmail/
import smtplib
from email.mime.text import MIMEText


def send_email(subject, body, sender, recipient, password):
    """
    Sends out mail to given recipient.

    params:
        subject: the subject of the email
        body: the body aka. actual content of the email
        sender: the email address which the mail is sent FROM
        recipient: the receiver's email address of the email
        password: the password (App password in gmail)
    """
    msg = MIMEText(body)
    msg["Subject"] = subject
    msg["From"] = sender
    msg["To"] = recipient
    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp_server:
       smtp_server.login(sender, password)
       smtp_server.sendmail(sender, recipient, msg.as_string())
    print(f"{recipient} got mail!")
