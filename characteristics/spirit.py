# -*- coding: utf-8 -*-
from characteristics.characteristic import Characteristic


class Spirit(Characteristic):
    BASE_SKILLS:  dict = {
        1: 'effort_of_will',
        2: 'power_of_ideals',
        3: 'persistance',
        4: 'trial_of_spirit',
        5: 'stronghold_of_faith'
    }
    persistence:  int = 0
