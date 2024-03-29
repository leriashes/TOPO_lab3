import unittest
from App.Cell import Cell

class TestCell(unittest.TestCase):
    
    def testCellClassCreation(self):
        cell = Cell()
        self.assertIsNotNone(cell)

    def testCellGetValue(self):
        cell = Cell()
        self.assertIsNotNone(cell.GetValue())

    def testCellGetCoords(self):
        cell = Cell()
        self.assertIsNotNone(cell.GetCoords())

    def testCellGetCoordsReturnTwoValues(self):
        cell = Cell()
        coords = cell.GetCoords()
        self.assertEqual(len(coords), 2)

    def testCellSetValue(self):
        cell = Cell()
        cell.SetValue(5)
        self.assertEqual(5, cell.GetValue())

    def testCellClassCreationWithParametersCheckValue(self):
        value = 15
        cell = Cell(value)
        self.assertEqual(value, cell.GetValue())

    def testCellClassCreationWithParametersCheckCoords(self):
        coords = [0, 0]
        cell = Cell(coords=coords)
        self.assertEqual(coords, cell.GetCoords())