import random

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
        