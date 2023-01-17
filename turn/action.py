from character import Character
from characteristics.dexterity import Dexterity
from characteristics.intelligence import Intelligence
from characteristics.strength import Strength


class Action:
    player: Character = None
    action_type: str = ''
    used_actions: list = []

    def __init__(self, start_charasteristics: dict):
        self.hits = start_charasteristics['constitution']*10
        self.constitution = start_charasteristics['constitution']
        self.strength = Strength(start_charasteristics['strength'])
        self.dexterity = Dexterity(start_charasteristics['dexterity'])
        self.intelligence = Intelligence(start_charasteristics['intelligence'])






