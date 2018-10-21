from direction import Direction
from copy import copy


class Snake:

    def __init__(self, coordinates):
        self.coordinates = [coordinates]
        self.length = 1
        self.direction = Direction.UP
        self.snake_should_grow = False

    def time_step(self):
        next_head_coordinate = self.get_next_head_coordinate()
        self.move_snake(next_head_coordinates)

    def get_next_head_coordinates(self):
        next_head_coordinate = copy(self.coordinates[0])
        if self.direction == Direction.UP:
            next_head_coordinate.decrement_y_coordinate(1)
        elif self.direction == Direction.DOWN:
            next_head_coordinate.increment_y_coordinate(1)
        elif self.direction == Direction.LEFT:
            next_head_coordinate.decrement_x_coordinate(1)
        else:
            next_head_coordinate.increment_x_coordinate(1)
        return next_head_coordinate

    def move_snake(self, next_head_coordinates):
        self.coordinates = [next_head_coordinates] + self.coordinates
        if not self.snake_should_grow:
            self.coordinates = self.coordinates[:-1]

    def set_snake_should_grow(self, snake_should_grow):
        self.snake_should_grow = snake_should_grow
            
    def check_self_collision(self):
        for coordinate in self.coordinates[1:]:
            if coordinate == self.coordinates[0]:
                return True
        return False
