import unittest
from App.Cell import Cell

class TestCell(unittest.TestCase):
    
    def testCellClassCreation(self):
        cell = Cell()
        self.assertIsNotNone(cell)

    def testCellGetValue(self):
        cell = Cell()
        self.assertIsNotNone(cell.getValue())

    def testCellGetCoords(self):
        cell = Cell()
        self.assertIsNotNone(cell.getCoords())

    def testCellGetCoordsReturnTwoValues(self):
        cell = Cell()
        coords = cell.getCoords()
        self.assertEqual(len(coords), 2)

    def testCellSetValue(self):
        cell = Cell()
        cell.setValue(5)
        self.assertEqual(5, cell.getValue())

    def testCellClassCreationWithParametersCheckValue(self):
        value = 15
        cell = Cell(value)
        self.assertEqual(value, cell.getValue())

    def testCellClassCreationWithParametersCheckCoords(self):
        coords = [0, 0]
        cell = Cell(coords=coords)
        self.assertEqual(coords, cell.getCoords())