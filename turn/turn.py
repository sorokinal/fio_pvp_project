# -*- coding: utf-8 -*-
# pylint: disable=too-few-public-methods
from typing import List
from character import Character
from data_input_helper import input_action_data
from turn.action.action import Action


class Turn:
    player: Character = None
    available_actions: List[Action]

    def __init__(self, game, player: Character):
        self.player = player
        self.available_actions = [Action(player),
                                  Action(player),
                                  Action(player)]

        """Turn and Name"""
        game.turn_counter += 1
        print(f'\nTurn {game.turn_counter} - '
              f'Player: {player.name}\n'
              f'______________')

        """Incoming actions"""
        print('Incoming actions: ', end='')
        for inc_act in self.player.incoming_actions:
            if self.player.incoming_actions.index(inc_act) != len(self.player.incoming_actions) - 1:
                print(inc_act.name, end=', ')
            else:
                print(inc_act.name, end='')
        print()
        """TODO: blocking"""

        self.player.incoming_actions.clear()
        """TODO: Make each cahracter has it´s own incoming_actions array (now somehow it´s common)"""

        """Hits"""
        print(f'{self.player.name}'
              f'´s Hits: {str(self.player.current_hits)}'
              f'/ {str(self.player.max_hits)}')

    def process(self, game):
        """Available actions"""
        # self.available_actions[0].name = 'Attack'
        print(f'Available actions: ', end='')
        for act in self.available_actions:
            if self.available_actions.index(act) != len(self.available_actions) - 1:
                print(act.name, end=', ')
            else:
                print(act.name)

        """Uses actions"""
        while self.available_actions:
            """Data_input_helper gets players from game and asks for action parameters"""
            action_data = input_action_data(game)
            """Creates action with parameters from action_data"""
            action = self.choose_action(action_data)
            action.use(action_data['goal'])

    def choose_action(self, action_data):
        # action = self.available_actions[action_data['action_num']]
        for action in self.available_actions:
            self.available_actions.remove(action)
            if not action.type:
                action.type = action_data['action_type']
            action.goal = action_data['goal']
            return action
