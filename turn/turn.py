from Character import Character
from turn.Action import Action
from characteristics.Dexterity import Dexterity
from characteristics.Intelligence import Intelligence
from characteristics.Strength import Strength


class Turn:
    player: Character = None
    available_actions: list = [Action(), Action(), Action()]
    used_actions: list = []

    def __init__(self, start_charasteristics: dict):
        self.hits = start_charasteristics['constitution']*10
        self.constitution = start_charasteristics['constitution']
        self.strength = Strength(start_charasteristics['strength'])
        self.dexterity = Dexterity(start_charasteristics['dexterity'])
        self.intelligence = Intelligence(start_charasteristics['intelligence'])






