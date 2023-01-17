# This is a sample Python script.
import os

from game import Game


# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    players_folder_path = os.path.dirname(__file__) + \
                          f'{os.sep}resources{os.sep}players{os.sep}'
    game = Game(players_data_path_list=[players_folder_path+'draft.json',
                                        players_folder_path+'montgomery.json'])
    print('')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
