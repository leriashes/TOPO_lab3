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

    def testGridMoveCellFalse(self):
        grid = Grid()

        self.assertIs(grid.moveCell(0, 0), False)

    def testGridMoveCellTrueResult(self):
        grid = Grid()
        x, y = 3, 2
        grid.moveCell(x, y)
        
        self.assertEqual(grid.getCellValue(x, y), 0)

    def testGridMoveCellFalseResult(self):
        grid = Grid()
        x, y = 0, 0
        value = grid.getCellValue(x, y)
        grid.moveCell(x, y)
        
        self.assertEqual(grid.getCellValue(x, y), value)

    def testGridMoveCellEmptyResult(self):
        grid = Grid()
        x, y = 3, 3
        grid.moveCell(x, y)
        
        self.assertEqual(grid.getCellValue(x, y), 0)

    def testGridGetEmptyCellCoords(self):
        grid = Grid()
        coords = grid.getEmptyCellCoords()

        self.assertEqual(grid.getCellValue(coords[0], coords[1]), 0)

    def testGridGetEmptyCellCoordsAfterShuffle(self):
        grid = Grid()
        grid.shuffleCells()
        coords = grid.getEmptyCellCoords()

        self.assertEqual(grid.getCellValue(coords[0], coords[1]), 0)

    def testGridMoveCellEmptyAfterShuffle(self):
        grid = Grid()
        grid.shuffleCells()
        x, y = grid.getEmptyCellCoords()

        grid.moveCell(x, y)
        
        self.assertEqual(grid.getCellValue(x, y), 0)

    def testGridMoveCellTrueRightAfterShuffle(self):
        grid = Grid()
        grid.shuffleCells()
        x, y = grid.getEmptyCellCoords()

        while y == 3:
            grid.shuffleCells()
            x, y = grid.getEmptyCellCoords()

        y += 1
        grid.moveCell(x, y)

        self.assertEqual(grid.getCellValue(x, y), 0)

    def testGridMoveCellTrueRightAfterShuffleMove(self):
        grid = Grid()
        grid.shuffleCells()
        x, y = grid.getEmptyCellCoords()

        while y == 3:
            grid.shuffleCells()
            x, y = grid.getEmptyCellCoords()

        y += 1
        value = grid.getCellValue(x, y)
        grid.moveCell(x, y)

        self.assertEqual(grid.getCellValue(x, y - 1), value)

