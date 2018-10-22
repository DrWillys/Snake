from tkinter import *
from GameWindow import Snake_Backend
from coordinates import Coordinates
from direction import Direction


class Board(Canvas):

    def __init__(self):
        self.height = 400
        self.width = 400
        self.pixel_size = 20
        super().__init__(width=400, height=400, 
            background="black", highlightthickness=0)
        self.bind_all("<Key>", self.on_key_pressed)
        self.snake_backend = Snake_Backend(int(self.height/self.pixel_size),
                                           int(self.width/self.pixel_size))
        self.draw_game_objects()
        self.after(100, self.on_timer)
        self.pack()

    def on_key_pressed(self, event):
        key = event.keysym
        if key == "Left":
            self.snake_backend.set_snake_direction(Direction.LEFT)
        elif key == "Right":
            self.snake_backend.set_snake_direction(Direction.RIGHT)
        elif key == "Up":
            self.snake_backend.set_snake_direction(Direction.UP)
        elif key == "Down":
            self.snake_backend.set_snake_direction(Direction.DOWN)
        
    def on_timer(self):
        self.snake_backend.time_step()
        self.draw_game_objects()
        self.after(100, self.on_timer)

    def draw_game_objects(self):
        self.delete(ALL)
        for game_object in self.snake_backend.get_game_objects():
            self.create_rectangle_at_coordinates(game_object)

    def create_rectangle_at_coordinates(self, game_object):
        x1 = game_object.x*self.pixel_size
        y1 = game_object.y*self.pixel_size
        x2 = x1 + self.pixel_size
        y2 = y1 + self.pixel_size
        self.create_rectangle(x1, y1, x2, y2, fill="white")

class Bla(Frame):

    def __init__(self):
        super().__init__()
                
        self.master.title('Snake')
        self.board = Board()
        self.pack()


def main():

    root = Tk()
    nib = Bla()
    root.mainloop()  


if __name__ == '__main__':
    main()
