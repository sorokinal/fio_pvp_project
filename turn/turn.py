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
        game.turn_counter += 1
        print(f'Ход {game.turn_counter}\n'
              f'Игрок: {player.name}')

    def process(self, game):
        while self.available_actions:
            print(f'Доступные действия: {self.available_actions}')
            action_data = input_action_data(game)
            action = self.choose_action(action_data)
            action.use(action_data['goal'])

    def choose_action(self, action_data):
        action = self.available_actions[action_data['action_num']]
        self.available_actions.remove(action)
        if not action.type:
            action.type = action_data['action_type']
        action.goal = action_data['goal']
        return action
