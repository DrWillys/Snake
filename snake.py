from direction import Direction
from copy import copy


class Snake:

    def __init__(self, coordinates, color):
        self.coordinates = [coordinates]
        self.direction = Direction.UP
        self.snake_should_grow = False
        self.color = color

    def time_step(self):
        next_head_coordinates = self.get_next_head_coordinates()
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
        else:
            self.snake_should_grow = False

    def set_snake_should_grow(self, snake_should_grow):
        self.snake_should_grow = snake_should_grow
            
    def check_self_collision(self):
        for coordinate in self.coordinates[1:]:
            if coordinate == self.coordinates[0]:
                return True
        return False

    def get_snake_head(self):
        return self.coordinates[0]

    def set_direction(self, direction):
        self.direction = direction
