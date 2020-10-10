import os

class MailPreview:
    @staticmethod
    def Preview(msg):
        with open("preview.html", "w", encoding="utf8") as f:
            f.write(msg)
        os.system("start preview.html")
