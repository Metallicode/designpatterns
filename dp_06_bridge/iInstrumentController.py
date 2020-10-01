import controllers


#controller interface
class PluginController:
    def Activate(self):pass

    def Set(self, data):pass

    def ConnectTo(self, plugin):pass

    def Func01(self, data):pass

    def Func02(self, data):pass



#concrete PluginControllers
class MousePluginController(PluginController):

    def ConnectTo(self, plugin):
        self._plugin = plugin
        self._controller = controllers.MouseController(self._plugin.Play)

    def Activate(self):
        self._controller.Start()

        


class  SequencerPluginController(PluginController):
    
    def ConnectTo(self, plugin):
        self._plugin = plugin
        self._controller = controllers.SequencerController().DefineFunc(self._plugin.Play)

    def Activate(self):
        self._controller.Run()

    def Set(self, data):
        self._controller.SetLoop(data)




