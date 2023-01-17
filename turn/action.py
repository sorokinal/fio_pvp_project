from character import Character


class Action:
    player: Character = None
    goal: Character = None

    def __init__(self, player):
        self.player = player
