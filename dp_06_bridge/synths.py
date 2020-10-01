import numpy as np
import matplotlib.pyplot as plt
from scipy import signal as sgl
import sounddevice as sd
from scipy.io import wavfile



#simple sine wave generator
class Sine:
    def __init__(self):
        self._fs = 44100.0
        self._freq = 440.0
        
    def setFreq(self, f):
        self._freq = f
        return self
        
    def play(self, length):
        t = np.arange(self._fs*length) / self._fs
        y = np.sin(2 * np.pi * self._freq * t)
        sd.play(y , self._fs)



#fm synth
class FM6:
    def __init__(self):
        self._fs = 44100.0
        self._carrier = 10

    def _norm(self,data):
        min_v = min(data)
        max_v = max(data)
        return np.array([((x-min_v) / (max_v-min_v)) for x in data])*2.0-1


    def setcarrier(self,freq):
         self._carrier = freq
         
    def makesound(self,freqA, length):
        modulator_frequency = freqA

        modulation_index = 1.0

        time = np.arange(self._fs*length) / self._fs
        modulator = np.sin(2.0 * np.pi * modulator_frequency * time) * modulation_index
        carrier = np.sin(2.0 * np.pi * self._carrier * time)

        product = np.zeros_like(modulator)

        for i, t in enumerate(time):
            product[i] = np.sin(2. * np.pi * (self._carrier * t + modulator[i]))

        y = self._norm(product)
        sd.play(y , self._fs)


#super saw
class SH2020:
    def __init__(self):
        self._fs = 44100.0


    def cloud_maker(self, freq , n, diff, length, octaver=True):
        t = np.arange(self._fs*length) / self._fs
        product = sgl.sawtooth(2 * np.pi * freq * t)
        
        for i in range(n):
            product += sgl.sawtooth(2 * np.pi * (freq-diff) * t)
            product += sgl.sawtooth(2 * np.pi * (freq+diff) * t)
            diff += diff
        if octaver == True:
            product += sgl.sawtooth(2 * np.pi * freq/2 * t)
            product += sgl.sawtooth(2 * np.pi * freq/4 * t)*0.5

        min_v = min(product)
        max_v = max(product)
        y = np.array([((x-min_v) / (max_v-min_v)) for x in product])*2.0-1
        sd.play(y , self._fs)


class Sampler:

    def __init__(self):
        self.InitSamples()


    def InitSamples(self):
        d1 = wavfile.read("data/bd.wav")
        d2 = wavfile.read("data/sd.wav")
        d3 = wavfile.read("data/hh.wav")
        d4 = wavfile.read("data/oh.wav")
        self._samps = [d1[1],d2[1],d3[1],d4[1]]        

    def _norm(self,data):
        min_v = min(data)
        max_v = max(data)
        return np.array([((x-min_v) / (max_v-min_v)) for x in data])*2.0-1


    def _repitch(self,sampIndex, val):
        newSampl = []
        for i in range(len(self._samps[sampIndex])):
            if i % val == 0:
                continue
            else:
                newSampl.append(self._samps[sampIndex][i])

        self._samps[sampIndex] = np.array(newSampl)



    def play_sample(self, val, speed):
        samp = None
        if val < 250:
            self._repitch(0, speed)
            samp = self._samps[0]
        elif val > 250 and val < 500:
            self._repitch(1, speed)
            samp = self._samps[1]
        elif val > 500 and val < 750:
            self._repitch(2, speed)
            samp = self._samps[2]
        elif val > 750 and val < 1000:
            self._repitch(3, speed)
            samp = self._samps[3]

        sd.play(self._norm(samp))




        

if __name__ == "__main__":
    
    fm6 = FM6()
    sin = Sine()
    sh = SH2020()
    samp = Sampler()

    #sh.cloud_maker(100, 5, 0.002, 1.0)
    #sin.setFreq(777).play(0.5)   
    #fm6.makesound(20, 1)
