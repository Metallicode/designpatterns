import synths


#plugin interface
class Plugin:
    def __init__(self):
        self._plugin = None      
    def Play(self, pitch, length):pass

    def Mod01(self, val):pass
    def Mod02(self, val):pass



#concrete plugins
class SinePlugin(Plugin):
    def __init__(self):
        self._plugin = synths.Sine()
        
    def Play(self, pitch, length):
        self._plugin.setFreq(pitch).play(length)

    def Mod01(self, val):
        self._plugin.setFreq(val)




class FM6Plugin(Plugin):
    def __init__(self):
        self._plugin = synths.FM6()
            
    def Play(self, pitch, length):
        self._plugin.makesound(pitch, length)

    def Mod01(self, val):
        self._plugin.setcarrier(val)

        

        
class SH2020Plugin(Plugin):
    def __init__(self):
        self._plugin = synths.SH2020()
        self._detune = 0.001
        self._oscCount = 5
    
        
    def Play(self, pitch, length):
        self._plugin.cloud_maker(pitch,self._oscCount,self._detune, length)

    def Mod01(self, val):
        self._detune = val

    def Mod2(self, val):
         self._oscCount = val
        



class SamplerPlugin(Plugin):
    def __init__(self):
        self._plugin = synths.Sampler()

    
    def Play(self, pitch, length):
        self._plugin.play_sample(pitch, length)

