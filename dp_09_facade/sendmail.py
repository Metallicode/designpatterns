import yagmail

class SendMail:
    def __init__(self, usermail):
        self._my_user_email = usermail

    def SendMails(self, recipients, msg, password):
        yag = yagmail.SMTP(self._my_user_email, password)
        yag.send(recipients, msg[0], [msg[1]])



