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
        self.available_actions = [Action(player)]
        #for i in game.action_number:
        #    self.available_actions.append(self, Action(player))

        """Turn and Name"""
        game.turn_counter += 1
        print(f'\nTurn {game.turn_counter} - '
              f'Player: {player.name}\n'
              f'______________')

        """Hits"""
        print(f'{self.player.name}'
              f'´s Hits: {str(self.player.hits)}'
              f'/ {str(self.player.constitution * 10)}')

        """Incoming actions"""
        print('Incoming actions: ', end='')
        for inc_act in self.player.incoming_actions:
            print(inc_act.name, end=', ')
        print()
        """TODO: blocking"""

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
            """Makes a transition of introduced data parameters to Action"""
            action = self.choose_action(action_data)

            """Applying incoming actions that havent´b been blocked???"""
        # for action in self.player.incoming_actions:
            # action.use(action.goal)

            action.use(action_data['goal'])

        """An attempt to make transition of action from outcoming to incoming"""
        # print(str(self.player.hits))
        # for action in self.player.outcoming_actions:
        #    for enemy in game.players:
        #        if enemy == action.goal:
        #            (game.get_player_by_name(self, action.goal)).incoming_actions.append(action)
        #            self.player.outcoming_actions.remove(action)
        #        else:
        #            print('Oops')





    def choose_action(self, action_data):
        # action = self.available_actions[action_data['action_num']]
        for action in self.available_actions:
            self.available_actions.remove(action)
            if not action.type:
                action.type = action_data['action_type']
            action.goal = action_data['goal']
            """Outcoming actions?"""
            # self.player.outcoming_actions.append(self, action)
            return action
