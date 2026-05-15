import random


#Becher Klasse erstellen
class Cup:
    def __init__(self, dice_list):
        self.dice_list = dice_list

#Methoden zum Becher schütteln und Würfel anzeigen
    def roll_dices(self):
      for dice in self.dice_list:
          if dice.in_cup:
              dice.roll_dice()

    def reset(self):
        for dice in self.dice_list:
            dice.in_cup = True
