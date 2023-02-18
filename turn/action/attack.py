from character import Character


class Attack:
    damage: int = 10
    name = 'Attack'

    def __init__(self, character: Character, goal: Character):
        """Takes character´s damage as base damage"""
        self.damage = character.damage
        self.use_attack(goal)
        self.apply_attack(goal)

    def use_attack(self, goal: Character):
        goal.incoming_actions.append(self)

    def apply_attack(self, character: Character):
        character.current_hits = character.current_hits - self.damage
