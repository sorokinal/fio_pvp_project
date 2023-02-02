# -*- coding: utf-8 -*-
from characteristics.characteristic import Characteristic


class Dexterity(Characteristic):
    BASE_SKILLS:  dict = {
        1: 'fast_dodge',
        2: 'dexterous_tripping',
        3: 'crit',
        4: 'instant_parry',
        5: 'circular_blocking'
    }
    skills: dict = {}
    crit:  int = 0
