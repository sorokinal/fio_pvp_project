import os

from game import Game
from turn.turn import Turn

if __name__ == '__main__':
    players_folder_path = os.path.dirname(__file__) + \
                          f'{os.sep}resources{os.sep}players{os.sep}'
    """create game"""
    game = Game(players_data_path_list=[players_folder_path+'draft.json',
                                        players_folder_path+'montgomery.json'])

    """game process circle"""
    while not game.check_for_winner():
        for player in game.characters:
            turn = Turn(player)

    print('The battle is over.')
