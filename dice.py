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

    def draw(self, window):
        """Zeichnet den weißen Würfel """""
        w = self.size * 40
        # Würfel zeichnen
        pygame.draw.rect(window, (255, 255, 255), (self.possition[0], self.possition[1], w, w))
        pygame.draw.rect(window, (0, 0, 0), (self.possition[0], self.possition[1], w, w), 2)
        
        # Zahl zeichnen
        font = pygame.font.Font(None, 32)
        text = font.render(str(self.value), True, (0, 0, 0))
        text_rect = text.get_rect(center=(self.possition[0] + w / 2, self.possition[1] + w / 2))
        window.blit(text, text_rect)