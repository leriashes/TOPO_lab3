from App.Cell import Cell

class Grid(object):
    
    def __init__(self):
        self.cells = []

        for i in range(16):
            self.cells.append(Cell((i + 1) % 16, [i // 4, i % 4]))
    
    def getCellValue(self, x:int, y:int):
        return self.cells[x * 4 + y].getValue()

    def shuffleCells(self):
        #todo реализовать перемешивание €чеек
        self.cells[0].setValue(0)
        self.cells[15].setValue(1)

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