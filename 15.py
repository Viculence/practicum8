def hide_screen():
    for _ in range(25):
        print()


def bulls_and_cows(guess, secret):
    bulls = 0
    cows = 0
    for i in range(4):
        if guess[i] == secret[i]:
            bulls += 1
        elif guess[i] in secret:
            cows += 1
    return bulls, cows


def main():
    secret_number = input('Введите 4-значное цисло без повторения цифр: ')

    while len(secret_number) != 4 or len(set(secret_number)) != 4 or \
            not secret_number.isdigit():
        print('Неверный ввод! Повторите попытку.')
        secret_number = input('Введите 4-значное цисло без повторения цифр: ')

    hide_screen()

    attempts = 10

    for attempt in range(attempts):
        guess = input(f'Попытка {attempt+1}/{attempts}. Введите число: ')

        while len(guess) != 4 or len(set(guess)) != 4 or not guess.isdigit():
            print('Неверный ввод! Повторите попытку.')
            guess = input(f'Попытка: {attempt+1}/{attempts}: Введите число: ')

        bulls, cows = bulls_and_cows(guess, secret_number)

        if bulls == 4:
            print('Победа!')
            break
        else:
            print(f'Быков: {bulls}; Коров: {cows}')

    else:
        print('Проигрыш!')

main()