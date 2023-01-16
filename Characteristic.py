class Characteristic:
    max_value:  int = None
    current_value: int = None
    max_skill_value: int = None
    current_skills: list = []
    max_mode: int = None
    current_mode: int = None

    def __init__(self):
        """initialising base values"""

    def update_current_value(self, items: int):
        self.current_value += items

    def update_current_mode(self, items: int):
        self.current_mode += items

    def update_current_skills(self, skill_range: str):
        self.current_skills.remove(skill_range)







