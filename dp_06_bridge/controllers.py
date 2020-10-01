from pynput.mouse import Controller, Listener
import threading



#concrete controller #01
class MouseController:
    def __init__(self, target):
        self._screenX = 1360
        self._screenY = 767
        self._target = target
        self._t = None

    def SetTarget(self, t):
        self._target = t

    def SetScreen(self, x, y):
        self._screenX = x
        self._screenY = y
        
    def _scaleToScreenSize(self, xMouse, yMouse):
          fx = int(((xMouse * 100) / self._screenX) +50)
          fy = (yMouse) / self._screenY          
          return fx, fy

    def _mouse_clicked(self, a,b,c,d):
        if d is True:
            self._target(*self._scaleToScreenSize(a,b))

    def _listen(self):
        with Listener(on_click=self._mouse_clicked) as listener:
            listener.join()

    def Start(self):
        self._t = threading.Thread(target=self._listen, args=())
        self._t.start()



from itertools import cycle
import time
class SequencerController:
    def __init__(self):
        self._sequence = cycle([])
        self._run = False
        self._speed = 120
        self._t = None
        self._func = None

    def DefineFunc(self, func):
        self._func = func
        return self

    def _loop(self):
        while self._run is True:
            if self._func is not None:
                self._func(next(self._sequence), self._getTime())
                time.sleep(self._getTime())
            
    def _getTime(self):    
        return 100/(60000 / self._speed)
    
    def Run(self):
        self._run = True
        self._t = threading.Thread(target=self._loop, args=())
        self._t.start()

    def SetLoop(self, values):
        self._sequence = cycle(values)

    def SetSpeed(self, speed):
        self._speed = cycle(speed)




if __name__ == "__main__":

    mc = MouseController(print)
    mc.Start()
    
##    sc = SequencerController(print)
##    sc.SetLoop([234,567,87,355])
##    sc.Run()
    
    
    
