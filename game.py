import os
os.system("cls")

import pygame


class Game:
    def __init__(self, players, cup, window):
        self.players = players
        self.cup = cup
        self.window = window
        self.rolls = 0
        self.max_rolls = 5
        self.play_button = pygame.Rect(430, 225, 140, 50)

    def handle_click(self, pos):
        if self.play_button.collidepoint(pos):
            if self.rolls < self.max_rolls:
                self.cup.roll_dices()
                self.rolls += 1
            return

        for dice in self.cup.dice_list:
            if dice.get_rect().collidepoint(pos):
                dice.toggle_in_cup()
                return

    def draw_play_button(self):
        font = pygame.font.SysFont(None, 36)

        pygame.draw.rect(self.window, (0, 0, 0), self.play_button)

        text = font.render("Wuerfeln", True, (255, 255, 255))
        text_rect = text.get_rect(center=self.play_button.center)
        self.window.blit(text, text_rect)

    def draw_rolls(self):
        font = pygame.font.SysFont(None, 28)
        text = font.render(f"Wurf: {self.rolls}/{self.max_rolls}", True, (0, 0, 0))
        self.window.blit(text, (420, 175))

    def game_won(self):
        for player in self.players:
            if player.score >= 100:
                print(f"{player.name} hat gewonnen!")
                return True
        return False
