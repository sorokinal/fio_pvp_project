# -*- coding: utf-8 -*-
import os

from game import Game

if __name__ == '__main__':
    players_folder_path = os.path.dirname(__file__) + \
                          f'{os.sep}resources{os.sep}players{os.sep}'
    """create game"""
    game = Game(players_data_path_list=[players_folder_path+'draft.json',
                                        players_folder_path+'montgomery.json'])
    game.process()
    print('\The battle is over.')
