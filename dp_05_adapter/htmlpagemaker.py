class HTMLPageMaker():
    def __init__(self):
        self._lines = None
        
    def write(self, data, tag):
        
        with open('log.html', 'r') as f:
            self._lines = f.readlines()

        newLst = self._lines[:-2] + [self._createTag(data, tag)] + self._lines[len(self._lines)-2:]
        
        with open('log.html', 'w') as f:
            f.writelines(newLst)

        self._lines = None
        

    def _createTag(self, data, tag):
        if tag == "p":
            return f"<p>{data}</p>\n"
        elif tag == "b":
            return f"<p><b>{data}</b></p>\n"




