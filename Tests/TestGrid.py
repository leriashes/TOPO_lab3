import unittest
from App.Grid import Grid

class TestGrid(unittest.TestCase):

    def testGridClassCreation(self):
        grid = Grid()
        self.assertIsNotNone(grid)