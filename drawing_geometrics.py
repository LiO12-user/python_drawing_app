import pygame
import pygame as pg

# drawing geometrics

class Screen:

    def __init__(self):
        self.x = 800
        self.y = 800

    def set_mode(self):
        screen = pg.display.set_mode((self.x, self.y))
        return screen


# init screen
s = Screen()
screen = s.set_mode()

class command_line():
    def __init__(self):
        pass


class drawing():

    def __init__(self):

        pass

    def draw_rectangle(self, x, y):
        pygame.draw.rect(screen, (235, 52, 52), (x, y, 100, 100), 0)

drawing = drawing()

while True:

    for event in pg.event.get():
        # player movement
        if event.type == pg.MOUSEBUTTONDOWN:
            drawing.draw_rectangle(100, 100)

    pg.display.update()