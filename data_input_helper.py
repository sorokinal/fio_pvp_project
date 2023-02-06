def input_action_data(game):
    action_num = input("Номер действия: ")
    action_type = input("Тип Действия: ")
    goal = input("Цель: ")
    if not game.is_player_with_name_exists(goal):
        print(f'Игрока с именем {goal} не существует')
        goal = input("Цель: ")
    goal = game.get_player_by_name(goal)
    return {
        "action_num": int(action_num),
        "action_type": action_type,
        "goal": goal
    }
