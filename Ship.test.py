import unittest
import random
from Ship import Ship

def random_cell(max_x=9, max_y=9) -> tuple[int, int]:
    return (round(random.random()*max_x), round(random.random()*max_y))

class TestShip(unittest.TestCase):

    def setUp(self) -> None:
        self.__SHIP_TYPES = {
            "carrier": 5,
            "battleship": 4,
            "cruiser": 3,
            "submarine": 3,
            "destroyer": 2,
        }

    def test_get_ship_names(self):
        ship_names = ["carrier", "battleship", "cruiser", "submarine", "destroyer"]
        for ship_name in Ship.get_ship_names():
            self.assertIn(ship_name, ship_names)

    def test_init_get_name(self):
        for ship_name in Ship.get_ship_names():
            self.assertEqual(Ship(ship_name).get_name(), ship_name)

    def test_init_get_size(self):
        ship_types = Ship.get__SHIP_TYPES__for_testing()
        for ship_name in Ship.get_ship_names():
            self.assertEqual(Ship(ship_name).get_size(), ship_types[ship_name])

    def test_init_get_cells(self):
        for ship_name in Ship.get_ship_names():
            ship = Ship(ship_name)
            self.assertIsInstance(ship.get_cells(), set)
            self.assertEqual(len(ship.get_cells()), 0)

    def test_init_get_cells_attacked(self):
        for ship_name in Ship.get_ship_names():
            ship = Ship(ship_name)
            self.assertIsInstance(ship.get_cells_attacked(), set)
            self.assertEqual(len(ship.get_cells_attacked()), 0)

    def test_add_cell(self):
        cell = random_cell()
        for ship_name in Ship.get_ship_names():
            ship = Ship(ship_name)
            ship.add_cell(cell)
            self.assertEqual(len(ship.get_cells()), 1)

    def test_has_sunk_no_cells(self):
        for ship_name in Ship.get_ship_names():
            ship = Ship(ship_name)
            self.assertTrue(ship.has_sunk())
    
    def test_has_sunk_one_cell(self):
        for ship_name in Ship.get_ship_names():
            ship = Ship(ship_name)
            ship.add_cell(random_cell())
            self.assertFalse(ship.has_sunk())
    
    def test_has_sunk_many_cells(self):
        for ship_name in Ship.get_ship_names():
            ship = Ship(ship_name)
            for _ in range(max(round(random.randint(1, 10)), 1)):
                ship.add_cell(random_cell())
            self.assertFalse(ship.has_sunk())

    def test_receive_attack_one_cell_hit(self):
        """Add and attack one cell, should return true"""
        for ship_name in Ship.get_ship_names():
            ship = Ship(ship_name)
            target_cell = random_cell()
            ship.add_cell(target_cell)
            self.assertTrue(ship.receive_attack(target_cell))
    
    def test_receive_attack_one_cell_miss(self):
        """Add one cell and attack another cell, should return false"""
        for ship_name in Ship.get_ship_names():
            ship = Ship(ship_name)
            target_cell = random_cell()
            ship.add_cell(target_cell)
            self.assertFalse(ship.receive_attack((0,0)))

        
if __name__ == '__main__':
    unittest.main()