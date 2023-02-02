# -*- coding: utf-8 -*-
# pylint: disable=too-few-public-methods
from typing import List

from character import Character
from turn.action.action import Action
from turn.action.main_action import MainAction
from turn.action.side_action import SideAction


class Turn:
    player: Character = None
    available_actions: List[Action]
    turn_counter = 0

    def __init__(self, player: Character):
        self.player = player
        self.available_actions = [MainAction(player),
                                  MainAction(player),
                                  SideAction(player)]
        self.turn_counter += 1
        print(f'turn number {self.turn_counter}: {player.name}')

    # def choose_action(self, marker: ActionMarker):
    #     for action in self.available_actions:
    #         if action.MARKER == marker:
    #             action.use_action()
