##Robot Parts
class Legs:
    def __init__(self):
        self.size = None

    def __repr__(self):
        return f"LEGS size: {self.size}"
    
class Arms:
    def __init__(self):
        self.length = None
        
    def __repr__(self):
        return f"ARMS length: {self.length}"
    
class Body:
    def __init__(self):
        self.power = None
        
    def __repr__(self):
        return f"BODY power: {self.power}"
    
class Head:
    def __init__(self):
        self.color = None
        
    def __repr__(self):
        return f"HEAD color: {self.color}"
    




##Builder Interface
class Builder:
    def getLegs(self): pass
    def getArms(self): pass
    def getBody(self): pass
    def getHead(self): pass    





##Concrete Builder 01
class DefenceRobotBuilder(Builder):
    def getLegs(self):
        legs = Legs()
        legs.size = "big"
        return legs
        
    def getArms(self):
        arms = Arms()
        arms.length = "full"
        return arms
    
    def getBody(self):
        body = Body()
        body.power = "max"
        return body
    
    def getHead(self):
        head = Head()
        head.color = "gray"
        return head
    

##Concrete Builder 02
class HomeRobotBuilder(Builder):
    def getLegs(self):
        legs = Legs()
        legs.size = "small"
        return legs
    
    def getArms(self):
        arms = Arms()
        arms.length = "half"
        return arms
    
    def getBody(self):
        body = Body()
        body.power = "economy"
        return body
    
    def getHead(self):
        head = Head()
        head.color = "pink"
        return head



#full item
class Robot:
    def __init__(self):
        self.__legs = None
        self.__arms = None
        self.__body = None
        self.__head = None


    def setLegs(self, legs):
        self.__legs = legs

    def setArms(self, arms):
        self.__arms = arms

    def setBody(self, body):
        self.__body = body

    def setHead(self, head):
        self.__head = head


    def __repr__(self):
        return f"ROBOT id{id(self)} \n{self.__legs}\n{self.__arms}\n{self.__body}\n{self.__head}"


#Director
class Director:
    __builder = None
   
    def SetBuilder(self, builder):
        self.__builder = builder    

    def GetRobot(self):
        bot = Robot()

        bot.setLegs(self.__builder.getLegs())
        bot.setArms(self.__builder.getArms())
        bot.setBody(self.__builder.getBody())
        bot.setHead(self.__builder.getHead())

        return bot











if __name__ == "__main__":
    
    director = Director()
    director.SetBuilder(DefenceRobotBuilder())

    test_robot = director.GetRobot()
    print(test_robot)


