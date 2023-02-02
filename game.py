# -*- coding: utf-8 -*-
import json
from typing import List

from character import Character


class Game:
    characters: List[Character] = []

    def __init__(self, players_data_path_list: []):
        print("Hi, Mthrfckers! Let's start the game!")
        self.add_players(players_data_path_list)

    def add_players(self, players_data_path_list: []):
        """Loads data from files and create characters
        :param players_data_path_list: list of json filepath"""
        for path in players_data_path_list:
            file = open(path)
            character_data = json.load(file)
            self.characters.append(Character(character_data))

    def check_players_turn(self):
        """сук лень"""

    def kick_death_players(self):
        for pers in self.characters:
            if pers.hits <= 0:
                self.characters.remove(pers)

    def check_for_winner(self):
        if len(self.characters) == 1:
            print(f'{self.characters[0].name} WIN!!!')
            return True
        return False
