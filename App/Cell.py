class Cell(object):
    value = 1

    def __init__(self, value=0):
        self.value = value
        #todo ����������� ���������� ��������� ������

    def GetValue(self):
        return self.value

    def SetValue(self, value):
        self.value = value

    def GetCoords(self):
        #todo ����������� ������� ��������� ������
        return [0, 0]


