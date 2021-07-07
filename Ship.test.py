import unittest
from Ship import Ship, ShipOrientation

class TestShip(unittest.TestCase):

    def test_create_ship(self):

        ship = Ship("Alpha", (3, 1), (0, 0))

        self.assertEqual(ship.get_name(), "Alpha")
        self.assertEqual(ship.get_size(), (3, 1))
        self.assertEqual(ship.get_start_cell(), (0, 0))
        self.assertEqual(ship.get_ship_orientation(), ShipOrientation.HORIZONTAL)
        
        # cell locations
        cells = ship.get_cell_locations()
        cells_expected = [(0, 0), (0, 1), (0, 2)]
        self.assertEqual(len(cells), len(cells_expected))
        for cell in cells_expected:
            self.assertIn(cell, cells)
        