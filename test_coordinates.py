import unittest
from coordinates import Coordinates


class CoordinatesTestCase(unittest.TestCase):
    def setUp(self):
        self.coordinates = Coordinates(50,50)

    def test_initial_coordinates(self):
        self.assertEqual(self.coordinates.x, 50)
        self.assertEqual(self.coordinates.y, 50)

    def test_increment_x_coordinate(self):
        self.coordinates.increment_x_coordinate(1)
        self.assertEqual(self.coordinates.x, 51)
        self.coordinates.increment_x_coordinate(10)
        self.assertEqual(self.coordinates.x, 61)

    def test_increment_y_coordinate(self):
        self.coordinates.increment_y_coordinate(1)
        self.assertEqual(self.coordinates.y, 51)
        self.coordinates.increment_y_coordinate(10)
        self.assertEqual(self.coordinates.y, 61)

    def test_decrement_x_coordinate(self):
        self.coordinates.decrement_x_coordinate(1)
        self.assertEqual(self.coordinates.x, 49)
        self.coordinates.decrement_x_coordinate(10)
        self.assertEqual(self.coordinates.x, 39)

    def test_decrement_y_coordinate(self):
        self.coordinates.decrement_y_coordinate(1)
        self.assertEqual(self.coordinates.y, 49)
        self.coordinates.decrement_y_coordinate(10)
        self.assertEqual(self.coordinates.y, 39)

    def test_equals(self):
        equal_coordinates = Coordinates(50,50)
        self.assertEqual(self.coordinates, equal_coordinates)


    def test_not_equals(self):
        not_equal_coordinates = Coordinates(55,55)
        self.assertNotEqual(self.coordinates, not_equal_coordinates)


if __name__ == "__main__":
    unittest.main()
