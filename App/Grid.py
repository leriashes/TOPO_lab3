import random
from App.Cell import Cell

class Grid(object):
    
    def __init__(self):
        self.cells = []

        for i in range(16):
            self.cells.append(Cell((i + 1) % 16, [i // 4, i % 4]))
    

    def getCellValue(self, x:int, y:int):
        return self.cells[x * 4 + y].getValue()


    def checkCompletable(self, values):
        N = 0

        for i in range(16):
            if values[i] != 0:
                k = 0
                
                for j in range(15 - i):
                    if values[i + j + 1] != 0:
                        if values[i + j + 1] < values[i]:
                            k += 1
                N += k

            elif values[i] == 0:
                N += (i // 4) + 1

        return N % 2 == 0


    def shuffleCells(self):
        values = [i % 16 for i in range(1, 17)]
        
        while True:
            random.shuffle(values)
            if self.checkCompletable(values):
                break

        for i in range(16):
            self.cells[i].setValue(values[i])


    def moveCell(self, x, y):
        value = self.getCellValue(x, y)

        if value == 0:
            return False
        else:
            emptx, empty = self.getEmptyCellCoords()

            if x == emptx and (y == empty + 1 or y == empty - 1) or y == empty and (x == emptx + 1 or x == emptx - 1):
                self.cells[x * 4 + y].setValue(0)
                self.cells[emptx * 4 + empty].setValue(value)
                return True
            else:
                return False


    def getEmptyCellCoords(self):
        for cell in self.cells:
            if cell.getValue() == 0:
                return cell.getCoords()

    def checkWin(self):
        for i in range(16):
            if self.cells[i].getValue() != (i + 1) % 16:
                return False
        return True
