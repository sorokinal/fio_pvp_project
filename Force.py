import math

from Characteristic import Characteristic


class Force(Characteristic):
    base_skills:  dict = {
        'S1': 'lightning_strike',
        'S2': 'counter_strike',
        'S3': 'fury',
        'S4': 'clipping',
        'S5': 'flurry_of_blows'
    }

    fury:  int = None

    def __init__(self):
        """initialising base values"""

    def update_fury(self, items: int):
        self.update_fury += items

    def lightning_strike(self, character: Character):
        character.additional_attac_action += 1

    def counter_strike(self, character: Character, goal: Character, blocking_attacks: list):
        accessible_block_count = math.floor(character.force.current_mode/3)
        if len(blocking_attacks) <= accessible_block_count:
            for attack in blocking_attacks:
                goal.current_attacks[attack].state.set('blocking')
        else:
            print(f'Not enough force mode for {len(blocking_attack)} attacks')

"""coming soon soon soon"""
"Вощм чёт в этом роде. Соответственно нужны будут классы персонажа, хода(скорее всего)" \
"Надо думать насчёт хранимых состояний. Я пока слабо втыкаю можно ли отменить отмену атаки, к примеру."



