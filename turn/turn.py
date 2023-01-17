from character import Character
from turn.main_action import MainAction
from turn.side_action import SideAction


class Turn:
    player: Character = None
    available_actions: list = []
    turn_list: list = []
    turn_counter = 0

    def __init__(self, player: Character):
        self.player = player
        self.available_actions = [MainAction(player),
                                  MainAction(player),
                                  SideAction(player)]
        self.turn_counter += 1
        print(f'turn number {self.turn_counter}: {player.name}')

