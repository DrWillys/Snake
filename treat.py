class Treat():
    def __init__(self, coordinates, color):
        self.coordinates = [coordinates]
        self.color = color

    def get_coordinates(self):
        return self.coordinates[0]
