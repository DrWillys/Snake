import unittest
import snake


class SnakeGameTestCase(unittest.TestCase):
    def setUp(self):
        self.snake = snake()

    def test_default_snake_coordinates(self):
        self.assertEqual(self.snake.coordinates, (50, 50))
