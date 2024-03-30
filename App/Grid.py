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
        return False

    def shuffleCells(self):
        values = [i % 16 for i in range(1, 17)]
        random.shuffle(values)

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