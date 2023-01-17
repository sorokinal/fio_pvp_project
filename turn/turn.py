from character import Character
from turn.action import MainAction
from turn.side_action import SideAction


class Turn:
    player: Character = None
    available_actions: list = []
    turn_list: list = []

    def __init__(self, player):
        self.player = player
        self.available_actions = [MainAction(player),
                                  MainAction(player),
                                  SideAction(player)]
