class AddressesProvider:
    def __init__(self):
        self._address = []
        self._read_data_from_file()

    def _read_data_from_file(self):
        with open("emails.txt") as f:
            content = f.readlines()
            for i in range(len(content)):
                if content[i] != "":
                    self._address.append(content[i][:-1])


    def GetEmails(self):
        return self._address
    
if __name__ == "__main__":
    ap = AddressesProvider()
    print(ap.GetEmails())
