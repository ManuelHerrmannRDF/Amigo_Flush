import os
os.system("cls")

import pygame

#Game Klasse erstellen
class Game:
    def __init__(self,players,cup,window):
        self.players = players
        self.cup = cup
        self.window = window
    
#Methoden zum starten des Spiels.

    def play_turn(self):
        for player in self.players:
            print(f"{player.name} ist am Zug.")
        
        

    def game_won(self):
        for player in self.players:
            if player.score >= 100:
                print(f"{player.name} hat gewonnen!")
                return True
        return False