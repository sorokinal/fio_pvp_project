from characteristics.dexterity import Dexterity
from characteristics.intelligence import Intelligence
from characteristics.strength import Strength


class Character:
    name: str = ''
    hits: int = 0
    determination: int = 0
    constitution: int = 0
    strength: Strength = None
    dexterity: Dexterity = None
    intelligence: Intelligence = None
    # wisdom: Wisdom = None
    # spirit: Spirit = None
    # charisma: Charisma = None

    def __init__(self, start_data: dict):
        self.name = start_data['name']
        self.hits = start_data['constitution'] * 10
        self.constitution = start_data['constitution']
        self.strength = Strength(start_data['strength'])
        self.dexterity = Dexterity(start_data['dexterity'])
        self.intelligence = Intelligence(start_data['intelligence'])






