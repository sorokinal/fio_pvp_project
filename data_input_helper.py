from turn.action.action_type import ActionType


def input_action_data(game):
    """Data_input_helper gets players from game and asks for action parameters"""

    action_type = input("Тип Действия (A, S, D): ")
    while incorrect_type(action_type):
        action_type = input("Тип Действия (A, S, D): ")

    goal = input("Цель: ")
    while not game.is_player_with_name_exists(goal):
        print(f'Игрока с именем {goal} не существует')
        goal = input('Цель: ')
    goal = game.get_player_by_name(goal)

    return {
        "action_type": action_type,
        "goal": goal
    }


def incorrect_type(tipe):
    for types in ActionType:
        if tipe == types:
            return False
