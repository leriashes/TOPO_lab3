import unittest
from App.Grid import Grid

class TestGrid(unittest.TestCase):

    def testGridClassCreation(self):
        grid = Grid()
        self.assertIsNotNone(grid)

    def testGridShuffleCellsReturnValueInInterval(self):
        grid = Grid()
        grid.shuffleCells()
        
        for i in range(16):
            cellValue = grid.getCellValue(i // 4, i % 4)
            self.assertIs(0 <= cellValue <= 15, True)

    def testGridShuffleCellsNoSameValues(self):
        grid = Grid()
        grid.shuffleCells()

        values = []

        for i in range(16):
            cellValue = grid.getCellValue(i // 4, i % 4)

            for j in range(len(values)):
                self.assertNotEqual(values[j], cellValue)

            values.append(cellValue)

    def testGridShuffleCells(self):
        grid = Grid()
        grid.shuffleCells()

        dif = 0

        for i in range(16):
            cellValue = grid.getCellValue(i // 4, i % 4)

            if (cellValue != (i + 1) % 16):
                dif += 1
             
        self.assertGreater(dif, 0)

    def testGridMoveCellTrue(self):
        grid = Grid()

        self.assertIs(grid.moveCell(3, 2), True)

    def testGridMoveCellEmpty(self):
        grid = Grid()

        self.assertIs(grid.moveCell(3, 3), False)