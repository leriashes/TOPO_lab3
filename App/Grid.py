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
        return True