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
            cellValue = grid.getCellValue(i / 4, i % 4)
            self.assertIs(0 <= cellValue <= 15, True)
