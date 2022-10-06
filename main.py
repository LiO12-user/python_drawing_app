import pygame
import pygame as pg


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


class Axis:

    def __init__(self):
        self.axis_x_array = []
        self.axis_y_array = []


axis = Axis()


class drawing_functions:

    def draw_vertical_line(self, start_x):
        pygame.draw.line(screen, (10, 110, 10), (start_x, 0), (start_x, 800), 1)

    def draw_horizontal_line(self, start_y):
        pygame.draw.line(screen, (10, 110, 10), (0, start_y), (800, start_y), 1)


drawing = drawing_functions()
i = 0


class Draw():

    def __init__(self):
        self.x_pos = 10
        self.y_pos = 10

    def draw(self):
        for x in range(80):
            drawing.draw_vertical_line(axis.axis_y_array[x])
            drawing.draw_horizontal_line(axis.axis_x_array[x])

    def initialize_axis(self):

        for i in range(80):
            axis.axis_y_array.append(self.y_pos * i)
            axis.axis_x_array.append(self.x_pos * i)
            print(f'y is: {axis.axis_y_array[i]}')
            print(f'x is: {axis.axis_x_array[i]}')

            i += 1


draw = Draw()

draw.initialize_axis()

while True:
    screen.fill((0, 0, 0))

    draw.draw()

    pg.display.update()
