import dice
import game 
import pygame

#Liste mit Würfeln
dice_list = []
dice_list.append(dice.Dice(0, True, 1, (0, 0), "red"))
dice_list.append(dice.Dice(0, True, 1, (0, 0), "blue"))
dice_list.append(dice.Dice(0, True, 1, (0, 0), "green"))
dice_list.append(dice.Dice(0, True, 1, (0, 0), "yellow"))
dice_list.append(dice.Dice(0, True, 1, (0, 0), "black"))
print(dice_list[0].value)
#spiel starten
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



