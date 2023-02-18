# -*- coding: utf-8 -*-
import json
from typing import List

from character import Character
from turn.turn import Turn


class Game:
    players: List[Character] = []
    turn_counter: int = 0
    action_number: int = 3

    def __init__(self, players_data_path_list: []):
        print("Hi, Mthrfckers! Let's start the game!\n")
        self.add_players(players_data_path_list)
        print("Today´s challengers: " + (self.players[0]).name + ' againts '+(self.players[1]).name)

    def process(self):
        """Checking the finish condition and creates Round with Turns for every player"""
        while not self.check_for_winner():
            print('\nRound ' + str(self.turn_counter))
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
        """Kicks dead people"""
        for pers in self.players:
            if pers.hits <= 0:
                print('\n' + pers.name + '´s Hits are below zero. ' + pers.name + ' is dead.\n')
                self.players.remove(pers)

    def check_for_winner(self):
        """WIN"""
        if len(self.players) == 1:
            print(f'{self.players[0].name} WINS!!!')
            return True
        return False

    def is_player_with_name_exists(self, name: str):
        """Checking player name for Action´s goal"""
        for player in self.players:
            if player.name == name:
                return True
        return False

    def get_player_by_name(self, name: str):
        """Choosing player by his name for Action´s goal"""
        for player in self.players:
            if player.name == name:
                return player
        return None
