import unittest
from snake import Snake
from direction import Direction
from coordinates import Coordinates


class SnakeTestCase(unittest.TestCase):
    def setUp(self):
        self.snake = Snake(Coordinates(50, 50))

    def test_default_snake_coordinates(self):
        self.assertEqual(self.snake.coordinates[0].x, 50)
        self.assertEqual(self.snake.coordinates[0].y, 50)

    def test_initial_length(self):
        self.assertEqual(self.snake.length, 1)

    def test_initial_direction(self):
        self.assertEqual(self.snake.direction, Direction.UP)

    def test_get_next_head_coordinates(self):
        self.assertEqual(self.snake.get_next_head_coordinates(), Coordinates(50,49))
        self.assertEqual(self.snake.get_next_head_coordinates(), Coordinates(50,49))


if __name__ == "__main__":
    unittest.main()
