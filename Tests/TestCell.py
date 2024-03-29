import unittest
from App.Cell import Cell

class TestCell(unittest.TestCase):
    
    def testCellClassCreation(self):
        cell = Cell()
        self.assertIsNotNone(cell)
