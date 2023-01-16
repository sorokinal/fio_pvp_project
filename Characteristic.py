import math


class Characteristic:
    value: int = 0
    mode: int = 0
    skills: dict = {}

    def __init__(self, value):
        self.value = value
        self.mode = value-10
        if value > 11:
            for i in range(math.floor((value-10)/2)):
                self.skills[i+1] = self.BASE_SKILLS[i+1]

    def update_current_value(self, items: int):
        self.current_value += items

    def update_current_mode(self, items: int):
        self.current_mode += items







