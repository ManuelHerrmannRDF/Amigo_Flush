import os
os.system("cls")

import pygame

pygame.init()

window= pygame.display.set_mode((1000, 500))
background = pygame.image.load("hintergrund_fläche.jpg")

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    window.fill((255, 255, 255))
    window.blit(background, (0, 0))
    pygame.display.update()
pygame.quit()


