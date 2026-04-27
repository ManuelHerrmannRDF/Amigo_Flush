

#Spieler erstellen
class Player:
    def __init__(self, name,scorecard,is_human,ai_difficulty):
        self.name = name
        self.scorecard = scorecard
        self.is_human = is_human
        self.ai_difficulty = ai_difficulty

#Methoden zum Spieler anzeigen

    def score_points_on_scorecard(self):
        pass

    def choose_dices(self):
        pass

    def reset(self):
        pass