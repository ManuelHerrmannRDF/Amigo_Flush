import pygame

CATEGORIES = [
    "Einser",
    "Zweier",
    "Dreier",
    "Vierer",
    "Fünfer",
    "Sechser",
    "Gesamt oben",
    "Bonus(35 Punkte ab 63 Punkten)",
    "Gesamt oben + Bonus",
    "3er Pasch",
    "4er Pasch",
    "Full House(25 Punkte)",
    "Kleine Straße(30 Punkte)",
    "Große Straße(40 Punkte)",
    "Kniffel(50 Punkte)",
    "Chance",
    "Gesamt unten",
    "Gesamt oben + Bonus + Gesamt unten"
]



#Klasse für Scoreboard erstellen
class Scoreboard:
    def __init__(self, points):
        self.points = points if points else [0] * len(CATEGORIES)

#Methoden zum Scoardboard
    def has_bonus(self):
        pass

    def sum(self):
        pass

    def score_points_on_scorecard(self):
        pass

    @staticmethod
    def draw_score_table(window, score_obj):
        font = pygame.font.SysFont("None", 24)
        x = 650
        y = 20
        line_height = 20
        
        BLACK = (0, 0, 0)
        
        # Header
        text = font.render("Kategorie | Punkte", True, BLACK)
        window.blit(text, (x, y))
        
        # Linien
        current_y = y + line_height
        for i, category in enumerate(CATEGORIES):
            points = score_obj.points[i] if i < len(score_obj.points) else 0
            text_str = f"{category}: {points}"
            text = font.render(text_str, True, BLACK)
            window.blit(text, (x, current_y))
            current_y += line_height