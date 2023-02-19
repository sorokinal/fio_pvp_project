# -*- coding: utf-8 -*-
# pylint: disable=too-few-public-methods
from typing import List
from character import Character
from data_input_helper import input_action_data
from turn.action.action import Action


def answer_check(item: str):
    answer = input(f'Would you like to ' + item + '? Yes(Y)/No(N)) ')
    while True:
        if answer == 'Y':
            return True
        elif answer == 'N':
            return False
        else:
            item = input("Didn´t get the answer, repeat it. Yes(Y)/No(N)")


class Turn:
    player: Character = None
    available_actions: List[Action]

    def __init__(self, game, player: Character):

        self.player = player
        self.player.available_actions = [Action(player),
                                         Action(player),
                                         Action(player)]

        game.turn_counter += 1
        print(f'\nTurn {game.turn_counter} - '
              f'Player: {player.name}\n'
              f'______________')

        self.show_hits()

        if len(self.player.incoming_actions) != 0:
            self.show_incoming_actions()

            if len(player.skills) != 0:
                self.show_skills()

                if answer_check('block something'):
                    for act in player.incoming_actions:
                        if answer_check(f'block {act.name} ({act.player.name})'):
                            blocking_action = input('Which action would you like to block with? ')
                            while self.incorrect_skill(blocking_action):
                                blocking_action = input('Didn´t get the answer. Repeat it: ')
                            for skill in self.player.skills:
                                if blocking_action == skill.name:
                                    self.player.skills.remove(skill)
                                    self.player.incoming_actions.remove(act)

                if len(player.incoming_actions) != 0:
                    self.show_incoming_actions()
            for action_to_apply in self.player.incoming_actions:
                action_to_apply.apply()
                print("All actions applied.")
                self.player.incoming_actions.clear()
            self.show_hits()

        """TODO: Make each character has it´s own incoming_actions array (now somehow it´s common)"""

    def process(self, game):
        """Shows available actions, asks for parameters, create action and then use it"""
        self.show_available_actions()
        self.show_skills()
        for action in self.player.available_actions:
            action_data = input_action_data(game)
            action.type = action_data['action_type']
            action.goal = (action_data['goal'])
            action.use()

    def show_hits(self):
        print(f'{self.player.name}'
              f'´s Hits: {str(self.player.current_hits)}'
              f'/ {str(self.player.max_hits)}')

    def show_skills(self):
        print('You have: ', end='')
        for skill in self.player.skills:
            print(f'{skill.name} ({self.player.name})', end=' ')
        print()

    def show_incoming_actions(self):
        print('Incoming actions: ', end='')
        for inc_act in self.player.incoming_actions:
            if self.player.incoming_actions.index(inc_act) != len(self.player.incoming_actions) - 1:
                print(f'{inc_act.name} ({inc_act.player.name})', end=', ')
            else:
                print(f'{inc_act.name} ({inc_act.player.name})', end='')
        print()

    def show_available_actions(self):
        print(f'Available actions: ', end='')
        for act in self.player.available_actions:
            if self.player.available_actions.index(act) != len(self.player.available_actions) - 1:
                print(act.name, end=', ')
            else:
                print(act.name)

    def incorrect_skill(self, item):
        for skill in self.player.skills:
            if item == skill.name:
                return False
