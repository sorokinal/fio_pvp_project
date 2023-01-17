from Character import Character
from characteristics.Dexterity import Dexterity
from characteristics.Intelligence import Intelligence
from characteristics.Strength import Strength


class Attack:
    gaoal: Character = None


    def __init__(self, start_charasteristics: dict):
        self.hits = start_charasteristics['constitution']*10
        self.constitution = start_charasteristics['constitution']
        self.strength = Strength(start_charasteristics['strength'])
        self.dexterity = Dexterity(start_charasteristics['dexterity'])
        self.intelligence = Intelligence(start_charasteristics['intelligence'])






