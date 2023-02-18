from turn.action.action_type import ActionType


def input_action_data(game):
    """Gets action´s position"""
    # action_num = input("Номер действия: ")

    """Gets action´s Type"""
    action_type = input("Тип Действия (A, S, D): ")
    while incorrect_type(action_type):
        action_type = input("Тип Действия (A, S, D): ")

    """Gets action´s Goal"""
    goal = input("Цель: ")
    while not game.is_player_with_name_exists(goal):
        print(f'Игрока с именем {goal} не существует')
        goal = input('Цель: ')
    goal = game.get_player_by_name(goal)

    """Returns parameters that have been set back to action_data(Turn)"""
    return {
        "action_type": action_type,
        "goal": goal
    }


def incorrect_type(tipe):
    for types in ActionType:
        if tipe == types:
            return False
