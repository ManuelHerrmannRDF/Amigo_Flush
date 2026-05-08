
#Klasse für die Regeln
# CATEGORIES außerhalb der Klasse definieren, damit es importierbar ist
CATEGORIES = {
    "Einser": 1,
    "Zweier": 2,
    "Dreier": 3,
    "Vierer": 4,
    "Fünfer": 5,
    "Sechser": 6,
    "Gesamt oben": None,
    "Bonus(35 Punkte ab 63 Punkten)": None,
    "Gesamt oben + Bonus": None,
    "3er Pasch": None,
    "4er Pasch": None,
    "Full House(25 Punkte)": None,
    "Kleine Straße(30 Punkte)": None,
    "Große Straße(40 Punkte)": None,
    "Kniffel(50 Punkte)": None,
    "Chance": None,
    "Gesamt unten": None,
    "Gesamt oben + Bonus + Gesamt unten": None
}

class Rules:
    def __init__(self):
        pass  # Initialisierung ohne Parameter

    def calculate_score(self, category, dice_values):
        if category in CATEGORIES:
            if category in ["Einser", "Zweier", "Dreier", "Vierer", "Fünfer", "Sechser"]:
                return sum(die for die in dice_values if die == CATEGORIES[category])
            elif category == "3er Pasch":
                if any(dice_values.count(die) >= 3 for die in set(dice_values)):
                    return sum(dice_values)
            elif category == "4er Pasch":
                if any(dice_values.count(die) >= 4 for die in set(dice_values)):
                    return sum(dice_values)
            elif category == "Full House(25 Punkte)":
                if len(set(dice_values)) == 2 and any(dice_values.count(die) == 3 for die in set(dice_values)):
                    return 25
            elif category == "Kleine Straße(30 Punkte)":
                if set([1, 2, 3, 4]).issubset(dice_values) or set([2, 3, 4, 5]).issubset(dice_values) or set([3, 4, 5, 6]).issubset(dice_values):
                    return 30
            
        # Weitere Kategorien können hier hinzugefügt werden
        return 0

