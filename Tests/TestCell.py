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