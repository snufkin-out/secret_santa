import data, mail_service

# IMPORTANT: Add your data here
sender = NotImplemented
password = NotImplemented

list_of_participants = data.get_participants("participants.csv")
data.hocus_pocus(list_of_participants)

for participant in list_of_participants:
    recipient = participant.email
    subject = f"Secret Santa assignment for {participant.name}"
    body = f"""\
        Hello {participant.name}!\n 
        It's time, you got assigned to buy a present for someone, but shuush, keep it secret!\n\n
        Your person is:\n
        {participant.gifts}\n\n
        Good luck finding a present!\n\n
    """

    mail_service.send_email(subject, body, sender, recipient, password)
