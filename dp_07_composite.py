import numpy as np
from scipy import signal as sgl
import matplotlib.pyplot as plt
import sounddevice as sd

#Component Interface
class Component:
    def Operation(self):pass
    def Add(self,component):pass


#Leaf
class SineFunction(Component):
    def __init__(self, freq, length=0.5):
        self._freq = freq
        self._len = length
        self._fs = 44100

    def Operation(self):
        t = np.arange(self._fs*self._len) / self._fs
        y = np.sin(2 * np.pi * self._freq * t)
        return y     


#Composite
class Composite(Component):
    def __init__(self, *args):
        self._components = []
        for i in args:
            self._components.append(i)

    def _norm(self, data):
        min_v = min(data)
        max_v = max(data)
        return np.array([((x-min_v) / (max_v-min_v)) for x in data])*2.0-1

    def Add(self,component):
        self._components.append(component)

    def Operation(self):
        if self._components[0] is not None:
            complexwav = np.zeros_like(self._components[0].Operation())

            for i in range(len(self._components)):
                complexwav+= self._components[i].Operation()
          
            return self._norm(complexwav)


#
def plot(s):
    data = s.Operation()
    plt.plot(np.arange(len(data)),data)
    plt.show()

def play(s):
    sd.play(s.Operation())



if __name__ == "__main__":

    s01 = SineFunction(2)
    mix01 = Composite(SineFunction(1), SineFunction(440), SineFunction(600))
    mix02 = Composite(SineFunction(2000), SineFunction(80))
    mix03 = Composite(mix02, SineFunction(3000), SineFunction(999))

    root = Composite(mix01, mix03,  SineFunction(10000))







        
