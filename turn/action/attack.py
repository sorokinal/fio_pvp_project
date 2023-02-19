from character import Character
from turn.action.action_type import ActionType


class Attack:
    damage: int = 10

    def __init__(self, player: Character, goal: Character):
        """Sends Attack to incoming_actions and then applies damage"""
        self.player = player
        self.type = ActionType.ATTACK
        self.name = self.type.name
        self.goal = goal

    def apply(self):
        self.goal.current_hits -= self.damage
