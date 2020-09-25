#AbstractPage
class AbstractPage:
    def __init__(self): pass

    def ClosePage(self): pass

    def RunPageCommand(self): pass

    def RenderPage(self):
        print(self._data)


#AbstractFactory
class AbstractPageFactory:
    @staticmethod
    def CreateMainPage(): pass

    @staticmethod
    def CreateInfoPage(): pass   


#ConcreteFactory 01
class StandardPageFactory(AbstractPageFactory):
    @staticmethod
    def CreateMainPage():
        return StandardMainPage()

    @staticmethod
    def CreateInfoPage():
        return StandardInfoPage()   


#ConcreteFactory 02
class PremiumPageFactory(AbstractPageFactory):
    @staticmethod
    def CreateMainPage():
        return PremiumMainPage()

    @staticmethod
    def CreateInfoPage():
        return PremiumInfoPage()   



#ConcreteFactory 03
##class CustomPageFactory(AbstractPageFactory):
##    @staticmethod
##    def CreateMainPage():
##        return CustomMainPage()
##
##    @staticmethod
##    def CreateInfoPage():
##        return CustomInfoPage()




    


#ConcretePages:
    
##01
class PremiumMainPage(AbstractPage):
    def __init__(self):
        self._command = "Running Premium Main Command"
        self._data = "Rendering Premium Main Page"

    def ClosePage(self): 
        print("Closing Premium Main Page")
        
    def RunPageCommand(self): 
        print(self._command)


##02
class PremiumInfoPage(AbstractPage):
    def __init__(self):
        self._command = "Running Premium Info Command"
        self._data = "Rendering Premium Info Page"

    def ClosePage(self): 
        print("Closing Premium Info Page")
        
    def RunPageCommand(self): 
        print(self._command)
        

##03
class StandardMainPage(AbstractPage):
    def __init__(self):
        self._command = "Running Standard Main Command"
        self._data = "Rendering Standard Main Page"

    def ClosePage(self): 
        print("Closing Standard Main Page")
        
    def RunPageCommand(self): 
        print(self._command)
        

##04
class StandardInfoPage(AbstractPage):
    def __init__(self):
        self._command = "Running Standard Info Command"
        self._data = "Rendering Standard Info Page"

    def ClosePage(self): 
        print("Closing Standard Info Page")
        
    def RunPageCommand(self): 
        print(self._command)
        




##05
##class StandardMainPage(AbstractPage):
##    def __init__(self):
##        self._command = "Running Custom Main Command"
##        self._data = "Rendering Custom Main Page"
##
##    def ClosePage(self): 
##        print("Closing Custom Main Page")
##        
##    def RunPageCommand(self): 
##        print(self._command)
        

##06
##class StandardInfoPage(AbstractPage):
##    def __init__(self):
##        self._command = "Running Custom Info Command"
##        self._data = "Rendering Custom Info Page"
##
##    def ClosePage(self): 
##        print("Closing Custom Info Page")
##        
##    def RunPageCommand(self): 
##        print(self._command)



#Client/Driver

if __name__ == "__main__":
    
    #factory = StandardPageFactory()

    #factory = PremiumPageFactory()
    factory = CustomPageFactory()





