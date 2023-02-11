def input_action_data(game):
    """Gets action´s position"""
    # action_num = input("Номер действия: ")

    """Gets action´s Type"""
    action_type: str = '1'
    while action_type != '0':
        action_type = input("Тип Действия (A, S, D): ")
        if action_type == 'A':
            break

    """Gets action´s Goal"""
    goal = input("Цель: ")
    if not game.is_player_with_name_exists(goal):
        print(f'Игрока с именем {goal} не существует')
        goal = input('Цель: ')
    goal = game.get_player_by_name(goal)

    """Returns parameters that have been set back to action_data(Turn)"""
    return {
        # "action_num": int(action_num),
        "action_type": action_type,
        "goal": goal
    }
