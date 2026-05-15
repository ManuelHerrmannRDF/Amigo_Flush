
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
            elif category == "Große Straße(40 Punkte)":
                if set([1, 2, 3, 4, 5]).issubset(dice_values) or set([2, 3, 4, 5, 6]).issubset(dice_values):
                    return 40
            elif category == "Kniffel(50 Punkte)":
                if any(dice_values.count(die) == 5 for die in set(dice_values)):
                    return 50
            elif category == "Chance":
                return sum(dice_values) 
            elif category in ["Gesamt oben", "Bonus(35 Punkte ab 63 Punkten)", "Gesamt oben + Bonus", "Gesamt unten", "Gesamt oben + Bonus + Gesamt unten"]:
                return 0  # Diese Kategorien werden separat berechnet, daher hier 0 zurückgeben
        return 0

    def calculate_bonus(self, upper_score):
        if upper_score >= 63:
            return 35
        return 0
    
    def calculate_upper_total(self, upper_scores):
        return sum(upper_scores)
    
    def calculate_lower_total(self, lower_scores):
        return sum(lower_scores)
    
    def calculate_grand_total(self, upper_score, bonus, lower_score):
        return upper_score + bonus + lower_score

    def calculate_total_score(self, upper_score, bonus, lower_score):
        return upper_score + bonus + lower_score
    
            
#Berechnung der Punkte für die Kategorien, Bonus und Gesamtscore

def calculate_score(category, dice_values):
    rules = Rules()
    return rules.calculate_score(category, dice_values)

def calculate_bonus(upper_score):
    rules = Rules()
    return rules.calculate_bonus(upper_score)

def calculate_upper_total(upper_scores):
    rules = Rules()
    return rules.calculate_upper_total(upper_scores)    

def calculate_lower_total(lower_scores):
    rules = Rules()
    return rules.calculate_lower_total(lower_scores)    

def calculate_grand_total(upper_score, bonus, lower_score):
    rules = Rules()
    return rules.calculate_grand_total(upper_score, bonus, lower_score)

#Nur fünf würfe maximal, pro durchgrang, pro spieler

def calculate_scoreboard_points(dice_values):
    rules = Rules()
    upper_scores = []
    lower_scores = []
    points_list = []

    for category in CATEGORIES:
        if category in ["Einser", "Zweier", "Dreier", "Vierer", "Fünfer", "Sechser"]:
            points = rules.calculate_score(category, dice_values)
            upper_scores.append(points)
        elif category == "Gesamt oben":
            points = rules.calculate_upper_total(upper_scores)
        elif category == "Bonus(35 Punkte ab 63 Punkten)":
            points = rules.calculate_bonus(rules.calculate_upper_total(upper_scores))
        elif category == "Gesamt oben + Bonus":
            upper_total = rules.calculate_upper_total(upper_scores)
            points = upper_total + rules.calculate_bonus(upper_total)
        elif category == "Gesamt unten":
            points = rules.calculate_lower_total(lower_scores)
        elif category == "Gesamt oben + Bonus + Gesamt unten":
            upper_total = rules.calculate_upper_total(upper_scores)
            bonus = rules.calculate_bonus(upper_total)
            lower_total = rules.calculate_lower_total(lower_scores)
            points = rules.calculate_grand_total(upper_total, bonus, lower_total)
        else:
            points = rules.calculate_score(category, dice_values)
            lower_scores.append(points)

        points_list.append(points)

    return points_list


def can_roll_dice(player):
    return player.rolls < 5

def can_fill_category(player, category):
    return category in CATEGORIES and category not in player.categories_filled

def is_game_over(player):
    return len(player.categories_filled) == len(CATEGORIES)

def reset_player(player):
    player.rolls = 0
    player.categories_filled.clear()


#Punkte für die Kategorien, Bonus und Gesamtscore berechnen

def calculate_category_score(category, dice_values):
    return calculate_score(category, dice_values)

def calculate_player_bonus(player):
    upper_scores = [calculate_category_score(cat, player.dice_values) for cat in CATEGORIES if cat in ["Einser", "Zweier", "Dreier", "Vierer", "Fünfer", "Sechser"] and cat in player.categories_filled]
    upper_total = calculate_upper_total(upper_scores)
    return calculate_bonus(upper_total)

def calculate_player_total_score(player):
    upper_scores = [calculate_category_score(cat, player.dice_values) for cat in CATEGORIES if cat in ["Einser", "Zweier", "Dreier", "Vierer", "Fünfer", "Sechser"] and cat in player.categories_filled]
    lower_scores = [calculate_category_score(cat, player.dice_values) for cat in CATEGORIES if cat not in ["Einser", "Zweier", "Dreier", "Vierer", "Fünfer", "Sechser"] and cat in player.categories_filled]
    upper_total = calculate_upper_total(upper_scores)
    bonus = calculate_bonus(upper_total)
    lower_total = calculate_lower_total(lower_scores)
    return calculate_grand_total(upper_total, bonus, lower_total)

def is_category_filled(player, category):
    return category in player.categories_filled

def fill_category(player, category):
    if can_fill_category(player, category):
        score = calculate_category_score(category, player.dice_values)
        player.score += score
        player.categories_filled.add(category)
        reset_player(player)

