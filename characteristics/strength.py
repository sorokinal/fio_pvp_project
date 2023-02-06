# -*- coding: utf-8 -*-
from characteristics.characteristic import Characteristic


class Strength(Characteristic):
    NAME = 'Сила'
    BASE_SKILLS:  dict = {
        1: 'lightning_strike',
        2: 'counter_strike',
        3: 'fury',
        4: 'clipping',
        5: 'flurry_of_blows'
    }
    fury:  int = 0

    def update_fury(self, items: int):
        self.fury += items

    # def lightning_strike(self, character: Character):
    #     character.additional_attac_action += 1

    # def counter_strike(self, goal: Character, blocking_attacks: list):
    #     accessible_block_count = math.floor(self.current_mode/3)
    #     if len(blocking_attacks) <= accessible_block_count:
    #         for attack in blocking_att
    #             acks:
    #             goal.current_attacks[attack].state.set('blocking')
    #     else:
    #         print(f'Not enough force mode for {len(blocking_attack)} attacks')

    # def fury(self, character: Character):
    #     self.update_fury(len(character.current_attacks))
    #     'TODO: add to attacks logic'
    #     'every fury item update all attacks damage to 1/2 force.current_mode'
    #
    # def clipping(self, character: Character, goal: Character):
    #     character.current_attacks += 1
    #     goal.force.current_value = \
    #         goal.force.current_value - \
    #         (math.floor(0,5*self.current_mode) + math.floor(0,5*self.fury))

    # def flurry_of_blows(self, character: Character, goals: list):
    #     accessible_goals_count = math.floor(self.current_mode/2)
    #     if len(goals) == accessible_goals_count:
    #         for goal in goals:
    #             character.current_attacks[attack] +=1
    #             character.current_attacks[-1].goal = goal
    #     elif len(goals) > accessible_goals_count:
    #         print(f'Not enough force mode for {len(goals)} goals')
    #     else:
    #         print(f'You have {accessible_goals_count-goals} attacks for '
    #               f'other goals')
