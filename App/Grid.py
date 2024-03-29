from App.Cell import Cell

class Grid(object):
    
    def __init__(self):
        self.cells = []

        for i in range(16):
            self.cells.append(Cell((i + 1) % 16, [i / 4, i % 4]))
    
    def getCellValue(self, x:int, y:int):
        return self.cells[x * 4 + y].getValue()

    def shuffleCells(self):
        #todo реализовать перемешивание €чеек
        self.cells[0].setValue(0)
        self.cells[15].setValue(1)

    def moveCell(self, x, y):
        if self.getCellValue(x, y) == 0:
            return False
        #todo реализовать проверку на возможность сдвига €чейки
        elif x == 0 and y == 0:
            return False

        #todo реализовать сдвиг €чейки
        if x == 3 and y == 2:
            self.cells[x * 4 + y].setValue(0)

        return True

    def getEmptyCellCoords(self):
        for cell in self.cells:
            if cell.getValue() == 0:
                return cell.getCoords()