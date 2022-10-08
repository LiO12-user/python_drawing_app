# Importing the library
import pygame

# Initializing Pygame
pygame.init()

# Initializing surface
surface = pygame.display.set_mode((400, 300))

# Initialing Color
color = (255, 0, 0)

# Drawing Rectangle
while True:
    pygame.draw.rect(surface, color, pygame.Rect(100, 100, 100, 100), 2 )
    pygame.display.flip()
