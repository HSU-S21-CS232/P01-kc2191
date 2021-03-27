import pygame
import os

#initialize the game
pygame.init()

#create the screen
screen = pygame.display.set_mode((800, 600))

# Title and Icon
pygame.display.set_caption("Space Invaders!")
icon = pygame.image.load("/Users/kevinchung/KC2191/p04-kc2191/alien.png")
pygame.display.set_icon(icon)

#Game Loop: if you want to move objects in the game, manipulate this loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False   