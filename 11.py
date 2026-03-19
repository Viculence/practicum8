def game(cities):
    cities_list = cities.split()
    
    if len(cities_list) == 0:
        return "Города не введены."

    if len(cities_list) == 1:
        return "Победитель: Петя."

    players = ["Петя", "Вася"]

    for i in range(1, len(cities_list)):
        if cities_list[i][0].lower() != cities_list[i - 1][-1].lower():
            loser = players[i % 2]
            winner = players[(i + 1) % 2]
            return f"{loser} нарушил правила! Победитель: {winner}."

    last_player = players[(len(cities_list) - 1) % 2]
    return f"Все правила соблюдены. Победитель: {last_player}."

cities_input = input("Введите города: ")
print(game(cities_input))
