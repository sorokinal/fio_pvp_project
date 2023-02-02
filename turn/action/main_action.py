# -*- coding: utf-8 -*-
# pylint: disable=no-self-use
# pylint: disable=unused-argument

from turn.action.action import Action


class MainAction(Action):

    MARKER = 'main'

    def use_attack(self, goal_name):
        print('')

    def use_skill(self, skill_name, goal_name=None):
        print('')
