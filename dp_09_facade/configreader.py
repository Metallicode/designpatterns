import json


class ConfigReader:
    def __init__(self):
        self._configuration_data = None
        self._read_configuration_file()

    def _read_configuration_file(self):
        with open("config.json") as json_data_file:
            self._configuration_data = json.load(json_data_file)


    def GetConfiguration(self, key):
        return self._configuration_data[key]

if __name__ == "__main__":
    cr = ConfigReader()
