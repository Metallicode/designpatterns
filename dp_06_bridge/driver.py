import iPlugin
import iInstrumentController


if __name__ == "__main__":
    #SinePlugin/FM6Plugin/SH2020Plugin
    p = iPlugin.SH2020Plugin()
    mc = iInstrumentController.SequencerPluginController()
    mc.ConnectTo(p)
    mc.Set([120,132,245,65,57,768])
    mc.Activate()
