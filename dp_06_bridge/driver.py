import iPlugin
import iInstrumentController


if __name__ == "__main__":
    #SinePlugin/FM6Plugin/SH2020Plugin/SamplerPlugin
    p = iPlugin.SH2020Plugin()
    mc = iInstrumentController.SequencerPluginController()
    mc.ConnectTo(p)
    mc.Set([(234,0.5),(567,0.5),(87,0.5),(355,0.5)])
    mc.Activate()
