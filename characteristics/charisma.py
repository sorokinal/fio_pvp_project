# # -*- coding: utf-8 -*-
from characteristics.characteristic import Characteristic


class Charisma(Characteristic):
    NAME = 'Харизма'
    BASE_SKILLS: dict = {
        1: 'overwhelming offensive',
        2: 'defensive formation',
        3: 'unity',
        4: 'intimidating banner',
        5: 'militant march'
    }

    unity: int = 0

    def update_unity(self, items: int):
        self.unity += items
