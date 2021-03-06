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

    def test_check_self_collision(self):
        self.assertFalse(self.snake.check_self_collision())
        self.snake.coordinates += [Coordinates(50, 50)]
        self.assertTrue(self.snake.check_self_collision())

    def test_snake_should_grow(self):
        self.assertFalse(self.snake.snake_should_grow)
        self.snake.set_snake_should_grow(True)
        self.assertTrue(self.snake.snake_should_grow)


if __name__ == "__main__":
    unittest.main()
