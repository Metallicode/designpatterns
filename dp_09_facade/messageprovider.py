import os

class MessageProvider:
    def __init__(self, known_files, signature):
        self._msg = None
        self._msg_title = None
        self._msg_file_name = None
        self.known_files = known_files
        self._msg_signature = signature
        
        if self._search_for_file() is True:
            with open(self._msg_file_name, encoding="utf8") as f:
                self._msg_title = next(f)
                data = f.read()             
                if data != "":
                    self._msg = data
            

    def _search_for_file(self):
        allFiles = os.listdir(path='.')
        for i in range(len(allFiles)):
            if allFiles[i] not in self.known_files:
                self._msg_file_name = allFiles[i]
                return True
        return False

    def _decorate(self, text):   
        for i in text.split():
            if i.startswith("*"):
                text = text.replace(i, f"<b>{i[1:]}</b>")
            elif i.startswith("#"):
                text = text.replace(i, f"<h1>{i[1:]}</h1>")
            elif i.startswith("&"):
                text = text.replace(i, f"<span style='color:red;'>{i[1:]}</span>")
            elif i.startswith("$"):
                text = text.replace(i, f"<span style='background-color: yellow;'>{i[1:]}</span>")
            elif i.startswith("^"):
                text = text.replace(i, f"<u>{i[1:]}</u>")

        return text
    
            
    def GetMessage(self):
        if self._msg is not None:    
            return (self._msg_title, "<body dir='rtl' style='text-align:right; direction:rtl;'><div dir='rtl'>"
                    + self._decorate(self._msg)
                    + "</div></body>"
                    + self._msg_signature)
        else:
            raise RuntimeError("no message file in directory")
    
if __name__ == "__main__":
    
    mp = MessageProvider(["log.db", "mailsluth.py", "addressesprovider.py", "messageprovider.py", "messagelogger.py", "sendmail.py","emails.txt" ])
    print(mp.GetMessage())
