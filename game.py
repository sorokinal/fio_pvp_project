import json

from character import Character


class Game:
    characters: list = []

    def __init__(self, players_data_path_list: []):
        print("Hi, Mthrfther! Let's start the game!")
        self.add_characters_data(players_data_path_list)

    def add_characters_data(self, players_data_path_list: []):
        for path in players_data_path_list:
            file = open(path)
            character_data = json.load(file)
            self.characters.append(Character(character_data))
        return character_data

