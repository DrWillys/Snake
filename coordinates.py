class Coordinates:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        if isinstance(other, Coordinates):
            return self.x == other.x and self.y == other.y
        return False

    def increment_x_coordinate(self, increment):
        self.x += increment

    def decrement_x_coordinate(self, increment):
        self.x -= increment

    def increment_y_coordinate(self, increment):
        self.y += increment

    def decrement_y_coordinate(self, decrement):
        self.y -= decrement

    
