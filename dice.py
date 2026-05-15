import random
import pygame

#Würfel Klasse erstellen
class Dice:
    def __init__(self, value, in_cup,size,possition,color):
        self.value = value
        self.in_cup = in_cup
        self.size = size
        self.possition = possition
        self.color = color

#Methoden zum Würfeln und Anzeigen des Würfels
    def roll_dice(self):
        self.value = random.randint(1, 6)

    def show(self):
        print(f"Würfel zeigt: {self.value}")

    def get_rect(self):
        w = self.size * 40
        return pygame.Rect(self.possition[0], self.possition[1], w, w)

    def toggle_in_cup(self):
        self.in_cup = not self.in_cup

    def draw(self, window):
        """Zeichnet den weißen Würfel """""
        rect = self.get_rect()
        dice_color = (255, 255, 255) if self.in_cup else (220, 220, 220)
        # Würfel zeichnen
        pygame.draw.rect(window, dice_color, rect)
        pygame.draw.rect(window, (0, 0, 0), rect, 2)

        if not self.in_cup:
            pygame.draw.rect(window, (0, 150, 0), rect, 4)
        
        # Zahl zeichnen
        font = pygame.font.Font(None, 32)
        text = font.render(str(self.value), True, (0, 0, 0))
        text_rect = text.get_rect(center=rect.center)
        window.blit(text, text_rect)
