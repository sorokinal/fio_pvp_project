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

    def __init__(self, player: Character):
        self.player = player

    def set_action_type(self, action_type: ActionType):
        self.type = action_type

    def set_action_goal(self, goal: Character):
        self.goal = goal

    def use(self):
        self.player.available_actions.remove(self)
        self.goal.incoming_actions.append(self.switch_action())

    def switch_action(self):
        if self.type == ActionType.ATTACK.value:
            return Attack(player=self.player, goal=self.goal)
        # if self.type == ActionType.DETERMINATION:
        #     return Determination()
        # if self.type == ActionType.SKILL:
        #     return Skill()
        return None
