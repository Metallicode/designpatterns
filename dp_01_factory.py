import time



####Item Interface
class AbstractMsg:
    def printMsg(self): pass

####Concrete Item #1
class EvenMsg(AbstractMsg):
    def __init__(self):
        self.evenmsg = "Time Is An Illusion..."

    def printMsg(self):
        print(self.evenmsg)

####Concrete Item #2
class OddMsg(AbstractMsg):
    def printMsg(self):
        with open("texts/msg.txt") as f:
            data = f.read().strip()
            print(data)



#### FACTORY ####
class MsgFactory:

    @staticmethod
    def _checkTime():
        return time.localtime()[4]%2 is 0

    @staticmethod
    def CreateMsg():
        if(MsgFactory._checkTime() is True):
            return EvenMsg()
        else:
            return OddMsg()



#Driver / Client
if __name__ == "__main__":

    MsgFactory.CreateMsg().printMsg()
