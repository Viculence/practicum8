def game(cities):
    cities_list = cities.split()
    for i in range(1, len(cities_list)):
        if cities_list[i][0].lower() != cities_list[i-1][-1].lower():
            return "Ты проиграл!"
    return "Ты выиграл!"

cities_input = input("Введите города: ")
print(game(cities_input))