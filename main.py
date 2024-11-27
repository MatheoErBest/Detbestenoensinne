import pygame
import random
import sys

# Window
pygame.init()
screen = pygame.display.set_mode((300, 300))
pygame.display.set_caption('hei')
screen.fill(0,0,0)

# Colors
black = (127, 127, 127, 255)
blue = (127, 127, 255, 255)
cyan = (127, 255, 255, 255)
gold = (255, 235, 127, 255)
gray = (222, 222, 222, 255)
green = (127, 255, 127, 255)
orange = (255, 210, 127, 255)
purple = (207, 143, 247, 255)
red = (255, 127, 127, 255)
violet = (246, 192, 246, 255)
yellow = (255, 255, 127, 255)
white = (255, 255, 255, 255)


# Main loop
run = True

while run:
    for event in pygam.event.get():
        if event.type == pygame.QUIT():
            run = False
    
    screen.update()



