import dice
import game 
import rules
import scoreboard
import pygame
import cup
import player
from pathlib import Path

#Liste mit Würfeln
dice_list = []
dice_list.append(dice.Dice(0, True, 1, (50, 50), (255, 255, 255)))
dice_list.append(dice.Dice(0, True, 1, (110, 50), (255, 255, 255)))
dice_list.append(dice.Dice(0, True, 1, (170, 50), (255, 255, 255)))
dice_list.append(dice.Dice(0, True, 1, (230, 50), (255, 255, 255)))
dice_list.append(dice.Dice(0, True, 1, (290, 50), (255, 255, 255)))

dice_cup = cup.Cup(dice_list)

#spiel starten
pygame.init()

window = pygame.display.set_mode((1000, 500))
PROJECT_DIR = Path(__file__).resolve().parent
background = pygame.image.load(PROJECT_DIR / "hintergrund_fläche.jpg")

# Scoreboard erstellen mit initialen Punkten (alle 0)
score_board = scoreboard.Scoreboard([0] * len(rules.CATEGORIES))
players = [
    player.Player("Spieler 1", score_board, True, None)
]
mein_spiel = game.Game(players, dice_cup, window)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mein_spiel.handle_click(event.pos)

    window.fill((255, 255, 255))
    #Spielfeld links
    window.blit(background, (0, 0))
    #Würfel zeichnen
    for die in dice_list:
        die.draw(window)
    #Scoreboard rechts als Tabelle
    scoreboard.Scoreboard.draw_score_table(window, score_board)
    mein_spiel.draw_play_button()
    mein_spiel.draw_rolls()

    pygame.display.update()

pygame.quit()



