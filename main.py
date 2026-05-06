import dice
import game 
import scoreboard
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

window = pygame.display.set_mode((1000, 500))
background = pygame.image.load("hintergrund_fläche.jpg")

# Scoreboard erstellen mit initialen Punkten (alle 0)
score_board = scoreboard.Scoreboard([0] * len(scoreboard.CATEGORIES))

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    window.fill((255, 255, 255))
    #Spielfeld links
    window.blit(background, (0, 0))
    #Scoreboard rechts als Tabelle
    scoreboard.Scoreboard.draw_score_table(window, score_board)

    pygame.display.update()

pygame.quit()



