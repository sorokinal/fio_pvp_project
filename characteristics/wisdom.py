# -*- coding: utf-8 -*-
# pylint: disable=unused-argument
import math

from character import Character
from characteristics.characteristic import Characteristic


class Wisdom(Characteristic):
    BASE_SKILLS: dict = {
        1: 'magic_cuts',
        2: 'magic_disease',
        3: 'enchantment',
        4: 'enchanted_barrier',
        5: 'charms_of_bane'
    }

    enchantment: int = 0

    def update_enchantment(self, items: int):
        self.enchantment += items

    def magic_cuts(self, character: Character, goal: Character):
        """Волшебные порезы (М1) - Атаки по Цели усиливаются на 1/2 Мод. Мудрости до конца боя, даёт 1 Зачарование
        (М3)."""
        character.additional_attack_damage += math.floor(self.current_mode / 2)
        self.update_enchantment(1)

    def magic_disease(self, character: Character, goals: list):
        """
        Магическая болезнь (М2) - Отнимает Хиты в размере Модификатора Мудрости у количества Целей,
        равного половине Модификатора Мудрости, даёт два Зачарования."""

        accessible_goals_count = math.floor(self.current_mode / 2)
        if len(goals) == accessible_goals_count:
            for goal in goals:
                character.current_attacks.add_attack()
                character.current_attacks[-1].goal = goal

        elif len(goals) > accessible_goals_count:
            print(f'Not enough wisdom mode for {len(goals)} goals')

        else:
            print(f'You have {accessible_goals_count - goals} spell charges left')
            answer = input('Are you sure with all goals? Yes(1)/No(0)')
            if answer == '1':
                for goal in goals:
                    character.current_attacks.add_attack()
                    character.current_attacks[-1].goal = goal
            elif answer == '0':
                print('Reaim the spell')
            else:
                answer = input('Your answer isn´t recognized, repeat it')
        self.update_enchantment(2)

    def enchanted_barrier(self, character: Character, goal: Character):
        """
        Blocks 1/3 wisdom mode Skills for the goal, grants +3 enchantment
        Заколдованный барьер (М4) - Блокирует количество Умений цели, равное трети Модификатора Мудрости,
        даёт три Зачарования."""
        print(self.defence_list)
        print('You have ' + str(
            math.floor(self.current_mode / 3)) + 'available spellblocks. Which spells would you like to block?')

        goal.spell_block_numb = int(math.floor(self.current_mode / 3))
        for spell in self.defence_list:
            answer: str = '?'
            while answer != '1' or '0':
                input('You want to block' + self.defence_list[spell] + '? Y(1)/N(0)')
                if answer == '1':
                    self.defence_list.pop(spell)
                    self.spell_block_numb -= 1
                elif answer == '0':
                    continue
                else:
                    print('Answer unrecognized. Repeat')
        self.update_enchantment(3)

    def charms_of_bane(self, character: Character, goal: Character):
        """Goal´s wisdom is lowed by 1/2 wisdom mode, grants +4 enchantment
        Чары проклятия (М5) - Снижает Мудрость Цели в размере половины Модификатора Мудрости плюс Зачарование,
        даёт четыре Зачарования."""
        goal.wisdom.update_current_value(-int(self.current_mode / 3))
        self.update_enchantment(4)

    # def enchantment(self, character: Character):
    #     class Spellcasting(SideAction):
    #         spell_total_time = 0
    #         spell_current_time = 0
    #         spell_effects:  dict = {
    #             1: 'Grants 10 Defence',
    #             2: 'Grants additional Attack',
    #             3: 'Blocks first Attack on Host',
    #             4: 'Doubles the power of the skill',
    #             5: 'Makes skill unblockable',
    #             6: 'Top up 1 characteristic for 1/2 wisdom mode',
    #             7: 'Skill is applied on 1/2 wisdom mode goals'
    #         }
    #
    #         def __init__ (self, spell_total_time):
    #             self.spell_total_time += spell_total_time
    #
    #         def spell_casting (self):
    #             if self.spell_current_time == spell_total_time:
    #                 self.spell_cast(self.enchantment)
    #             else:
    #                 self.spell_current_time += 1
    #
    #         def spell_cast (self, enchantment):
    #             'use self.spell_effects[self.enchantment]'
