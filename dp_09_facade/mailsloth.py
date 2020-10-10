from addressesprovider import AddressesProvider
from messageprovider import MessageProvider
from messagelogger import MessageLogger
from sendmail import SendMail
from configreader import ConfigReader
from previewmail import MailPreview


class MailSloth:
    def __init__(self):
        self._configreader = ConfigReader()
        self._addressesprovider = AddressesProvider()
        self._messageprovider = MessageProvider(self._configreader.GetConfiguration("known_files"), self._configreader.GetConfiguration("signature"))
        self._messagelogger = MessageLogger()
        self._mailsender = SendMail(self._configreader.GetConfiguration("sender_email"))
        self._previewmail = MailPreview()
        self._previewmail.Preview(self._messageprovider.GetMessage()[1])

    def Send(self, password):
        msg = self._messageprovider.GetMessage()
        self._mailsender.SendMails(self._addressesprovider.GetEmails(),msg,password)    
        self._messagelogger.LogMessage(msg)

        
if __name__ == "__main__":
    ms = MailSloth()    
    ms.Send(input())
