class Cell(object):
    value = 1

    def __init__(self, value=0):
        self.value = value
        #todo реализовать сохранение координат €чейки

    def GetValue(self):
        return self.value

    def SetValue(self, value):
        self.value = value

    def GetCoords(self):
        #todo реализовать возврат координат €чейки
        return [0, 0]


