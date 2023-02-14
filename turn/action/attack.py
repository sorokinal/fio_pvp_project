from character import Character


class Attack:
    damage: int = 10

    def __init__(self, character: Character, goal: Character):
        """Takes character´s damage as base damage"""
        self.damage = character.damage
        self.use_attack(goal)

        """Whoa?"""
        'TODO: Switch from input_attacks to outcoming_actions'
        # self.use_attack(goal)

        """Deals Damage"""
        self.apply_attack(goal)

    def use_attack(self, goal: Character):
        goal.input_attacks.append(self)

    def apply_attack(self, character: Character):
        character.hits = character.current_hits - self.damage
