# -*- coding: utf-8 -*-
# pylint: disable=too-few-public-methods
from characteristics.constitution import Constitution
from characteristics.dexterity import Dexterity
from characteristics.intelligence import Intelligence
from characteristics.strength import Strength
from characteristics.wisdom import Wisdom
from characteristics.spirit import Spirit
from characteristics.charisma import Charisma


class Character:
    name: str = ''
    max_hits: int = 0
    current_hits: int = 0
    determination: int = 0

    """Characteristics"""
    constitution: Constitution = None
    strength: Strength = None
    dexterity: Dexterity = None
    intelligence: Intelligence = None
    wisdom: Wisdom = None
    spirit: Spirit = None
    charisma: Charisma = None

    turn: int = 1
    skills = []
    incoming_actions = []
    available_actions = []

    def __init__(self, start_data: dict):
        self.turn = start_data['turn']
        self.name = start_data['name']
        self.max_hits = start_data['constitution'] * 10
        self.current_hits = self.max_hits

        """Characteristics"""
        self.constitution = start_data['constitution']
        self.strength = Strength(start_data['strength'])
        self.dexterity = Dexterity(start_data['dexterity'])
        self.intelligence = Intelligence(start_data['intelligence'])
        self.wisdom = Wisdom(start_data['dexterity'])
        self.spirit = Spirit(start_data['dexterity'])
        self.charisma = Charisma(start_data['dexterity'])
