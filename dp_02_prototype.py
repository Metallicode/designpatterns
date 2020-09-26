import copy
import time







#Prototype Interface
class Prototype:
    def Clone(self): pass









#Concrete Prototype 1
class Audible(Prototype):
    def __init__(self, audible_type, args=None):
        self.type = audible_type
        #time.sleep(0.001)
        self.args = args

    def play(self): pass
    
    def Clone(self):
        return  copy.deepcopy(self)   


#Concrete Prototype 2
class Visual(Prototype):
    def __init__(self, data):
        self._data = data

    def show(self):
        print(f"show data from {self._data}")
    
    def Clone(self):
        return  copy.deepcopy(self)   








#Prototype Factory
class PrototypeFactory:
    def __init__(self, AudiblePrototype_A, AudiblePrototype_B, VisualPrototype_A):
        self._prototype_A = AudiblePrototype_A
        self._prototype_B = AudiblePrototype_B
        self._prototype_C = VisualPrototype_A
        
    def GetCopy(self, t):
        if (t is "a"):
            return self._prototype_A.Clone()
        elif (t is "b"):
            return self._prototype_B.Clone()
        elif (t is "x"):
            return self._prototype_C.Clone()








#test
def func_new_obj():
    start = time.time()
    x = None
    for i in range(1000):
        x = Audible("Hifi", [1,2,3])

    print(f"bye {(time.time() - start) }")



def func_copy_prototype():
    start = time.time()
    x = None
    for i in range(1000):
        x = PrototypeFactory.GetCopy("a")

    print(f"bye {(time.time() - start) }")






#Driver
if __name__  == "__main__":
    
    p1 = Audible("Hifi", [1,2,3])
    p2 = Audible("Lofi", [6,5,4])
    p3 = Visual("data/at/path/file.img")

    PrototypeFactory = PrototypeFactory(p1,p2,p3)
    
    c1 = PrototypeFactory.GetCopy("a")
    c2 = PrototypeFactory.GetCopy("b")
    c3 = PrototypeFactory.GetCopy("a")

    c4 = PrototypeFactory.GetCopy("x")
    
    print(f"c1 is c3: {c1 is c3}")
    print(f"c1.args: {c1.args}")
    print(f"c3.args: {c3.args}")
    print(f"c1.args is c3.args: {c1.args is c3.args}")
    c1.args[0] = 100
    c3.args[2] = 999
    print(f"c1.args after change: {c1.args}")
    print(f"c3.args after change: {c3.args}")
    c5 = PrototypeFactory.GetCopy("a")
    print(f"c5.args: {c5.args}")

    func_new_obj()
    func_copy_prototype()
