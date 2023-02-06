# -*- coding: utf-8 -*-
from characteristics.characteristic import Characteristic


class Intelligence(Characteristic):
    NAME='Интеллект'
    BASE_SKILLS:  dict = {
        1: 'mental_pain',
        2: 'intellect_pressure',
        3: 'progress',
        4: 'tactical_retreat',
        5: 'strategic_offensive'
    }
    skills: dict = {}
    progress:  int = 0
