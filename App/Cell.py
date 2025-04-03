class Cell(object):

    def __init__(self, value=0, coords=[0,0]):
        self.value = value
        self.coords = coords

    def getValue(self):
        return self.value

    def setValue(self, value):
        self.value = value

    def getCoords(self):
        return self.coords
