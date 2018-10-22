from tkinter import *
from snake import Snake
from treat import Treat
from coordinates import Coordinates
from random import choice
from copy import copy


class Snake_Backend():
    def __init__(self, height, width):
        self.height = height
        self.width = width
        self.game_coordinates = self.calculate_game_coordinates()
        self.snake = Snake(Coordinates(4,4), "blue")
        self.treat = None

    def calculate_game_coordinates(self):
        coordinates = []
        for i in range(self.height):
            for j in range(self.width):
                coordinates += [Coordinates(i,j)]
        return coordinates

    def time_step(self):
        if self.should_spawn_treat():
            self.spawn_treat()
        if self.snake_has_eaten_treat():
            self.snake.set_snake_should_grow(True)
            self.treat = None
        self.snake.time_step()
        if self.is_snake_outside_game_area():
            print("Game Over")
        if self.snake.check_self_collision():
            print("Game Over")

    def should_spawn_treat(self):
        return self.treat is None

    def spawn_treat(self):
        unoccupied_coordinates = self.get_unoccupied_coordinates()
        self.treat = Treat(choice(unoccupied_coordinates), "green")

    def get_unoccupied_coordinates(self):
        unoccupied_coordinates = []
        for coordinates in self.game_coordinates:
            for snake_coordinates in self.snake.coordinates:
                if coordinates != snake_coordinates:
                    unoccupied_coordinates += [coordinates]
        return unoccupied_coordinates

    def snake_has_eaten_treat(self):
        return self.snake.get_snake_head() == self.treat.get_coordinates()
            
    def is_snake_outside_game_area(self):
        snake_head = self.snake.get_snake_head()
        if snake_head.x < 0:
            return True
        elif snake_head.x >= self.width:
            return True
        elif snake_head.y < 0:
            return True
        elif snake_head.y >= self.height:
            return True
        return False

    def set_snake_direction(self, snake_direction):
        self.snake.set_direction(snake_direction)

    def get_game_objects(self):
        game_objects = copy(self.snake.coordinates)
        if self.treat is not None:
            game_objects += self.treat.coordinates
        return game_objects
