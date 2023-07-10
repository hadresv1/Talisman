import pygame
import numpy
import time




screen = pygame.display.set_mode((640, 240))
YELLOW = (255, 255, 0)
RED = (255, 0, 0)
GRAY = (127, 127, 127)
background = GRAY
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                background = RED
            elif event.key == pygame.K_g:
                background = YELLOW

        screen.fill(background)
        pygame.display.update()



        if event.type == pygame.QUIT:
            running = False

pygame.quit()