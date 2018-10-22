from tkinter import *
from snake import Snake
from treat import Treat
from coordinates import Coordinates
from random import choice


class GameWindow():
    def __init__(self):
        self.height = 400
        self.widht = 400
        self.pixel_size = 20
        self.snake = Snake(Coordinates(4,4))
        self.treat = None

    def time_step(self):
        if self.should_spawn_treat():
            self.spawn_treat()
        if self.snake_has_eaten_treat():
            self.snake.set_snake_should_grow(True)
        if self.is_snake_outside_game_area():
            print("Game Over")
        if self.snake.check_self_collision():
            print("Game Over")

    def is_snake_outside_game_area(self):
        snake_head = self.snake.get_snake_head()
        if snake_head.x < 0:
            return True
        elif snake_head.x*self.pixel_size > self.width - self.pixel_size:
            return True
        elif snake_head.y < 0:
            return True
        elif snake_head.y*self.pixel_size > self.height - self.pizel_size:
            return True
        return False
    
    def snake_has_eaten_treat(self):
        return self.snake.get_snake_head() == self.treat.get_coordinates()
    
    def should_spawn_treat(self):
        return self.treat is None
    
    def spawn_treat(self):
        unoccupied_coordinates = self.get_unoccupied_coordinates()
        self.treat = Treat(choice(unoccupied_coordinates))

    def get_unoccupied_coordinates(self):
        all_coordinates = self.get_all_coordinates()
        unoccupied_coordinates = []
        for coordinate in all_coordinates:
            for snake_coordinate in self.snake.coordiantes:
                if coordinate != snake.coordinate:
                    unoccupied_coordinates += [coordinate]
        return unoccupied_coordinates

    def get_all_coordinates(self):
        coordinates = []
        for i in range(self.height/self.pixel):
            for j in range(self.lenght/self.pixel_coordinates):
                coordinates += [Coordinates(i,j)]
        return coordinates
