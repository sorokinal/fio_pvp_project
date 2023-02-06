# -*- coding: utf-8 -*-
import json
from typing import List

from character import Character
from turn.turn import Turn


class Game:
    players: List[Character] = []
    turn_counter: int = 0

    def __init__(self, players_data_path_list: []):
        print("Hi, Mthrfckers! Let's start the game!")
        self.add_players(players_data_path_list)

    def process(self):
        """game process circle"""
        while not self.check_for_winner():
            for player in self.players:
                turn = Turn(self, player)
                turn.process(self)
                self.kick_death_players()

    def add_players(self, players_data_path_list: []):
        """Loads data from files and create players
        :param players_data_path_list: list of json filepath"""
        for path in players_data_path_list:
            file = open(path)
            character_data = json.load(file)
            self.players.append(Character(character_data))

    def check_players_turn(self):
        """сук лень"""

    def kick_death_players(self):
        for pers in self.players:
            if pers.hits <= 0:
                self.players.remove(pers)

    def check_for_winner(self):
        if len(self.players) == 1:
            print(f'{self.players[0].name} WIN!!!')
            return True
        return False

    def is_player_with_name_exists(self, name: str):
        for player in self.players:
            if player.name == name:
                return True
        return False

    def get_player_by_name(self, name: str):
        for player in self.players:
            if player.name == name:
                return player
        return None
