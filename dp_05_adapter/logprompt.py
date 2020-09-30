#logger interface
class Logger:
    def log(self, msg): pass




#concrete logger 01
class SimpleLogger(Logger):
    def log(self, msg):
        print(msg)

#concrete logger 02
from datetime import datetime as dt
class TextfileLogger(Logger):    
    def log(self, msg):    
        with open("log.txt", "a") as f:
            f.write(f"{dt.now()} >>> {msg}\n")




#concrete logger 03 - WRONG INTERFACE!
from htmlpagemaker import HTMLPageMaker



#Adapter 
class HTMLPageMakerAdapter(Logger):
    def __init__(self):
        self._htmllogger = HTMLPageMaker()
        self._tagtype = "p"

    def SetLoggerTag(self, tag):
        self._tagtype = tag
        return self
        
    def log(self, msg):        
        self._htmllogger.write(msg, self._tagtype) 
    






#driver
if __name__ == "__main__":

    logger = HTMLPageMakerAdapter().SetLoggerTag("b")
    
    while True:
        msg = input("Please log your message:\n")
        logger.log(msg)
