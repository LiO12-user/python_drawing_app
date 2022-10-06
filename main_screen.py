import  pygame as pg

class Screen:

    def __init__(self):
        self.x = 800
        self.y = 800

    def set_mode(self):
        screen = pg.display.set_mode((self.x, self.y))
        return screen
