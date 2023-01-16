from Dexterity import Dexterity
from Intelligence import Intelligence
from Strength import Strength


class Character:
    hits: int = 0
    determination: int = 0
    constitution: int = 0
    strength: Strength = None
    dexterity: Dexterity = None
    intelligence: Intelligence = None
    # wisdom: Wisdom = None
    # spirit: Spirit = None
    # charisma: Charisma = None

    def __init__(self, start_charasteristics: dict):
        self.hits = start_charasteristics['constitution']*10
        self.constitution = start_charasteristics['constitution']
        self.strength = Strength(start_charasteristics['strength'])
        self.dexterity = Dexterity(start_charasteristics['dexterity'])
        self.intelligence = Intelligence(start_charasteristics['intelligence'])






