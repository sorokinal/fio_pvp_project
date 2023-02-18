# -*- coding: utf-8 -*-
# pylint: disable=too-few-public-methods
from character import Character
from turn.action.action_type import ActionType
from turn.action.attack import Attack


class Action:
    name: str = 'Main Action'
    type: ActionType = None
    player: Character = None
    goal: Character = None

    def __init__(self, player):
        self.player = player

    def set_action_type(self, action_type: ActionType):
        self.type = action_type

    def use(self, goal: Character = None):
        if self.type == ActionType.ATTACK.value:
            return Attack(character=self.player, goal=goal)
        return None
        # if self.type == ActionType.DETERMINATION:
        #     return Determination()
        # if self.type == ActionType.SKILL:
        #     return Skill()
