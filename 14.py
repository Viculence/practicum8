def field_of_dreams():
    tip = input()
    word = input().lower()

    for _ in range(25):
        print()

    symbols = ['*'] * len(word)
    attempts = 10

    print(tip)
    print(''.join(symbols))

    while attempts > 0:
        choice = input('Буква или слово (0 - буква, 1 - слово)?')
        attempts -= 1

        if choice == '0':
            letter = input().lower()
            for i, ch in enumerate(word):
                if ch == letter:
                    symbols[i] = letter
            print(''.join(symbols))

            if '*' not in symbols:
                print('Победа!')
                return

        elif choice == '1':
            guess = input().lower()
            if guess == word:
                print('Победа!')
                return
            else:
                print('Проигрыш!')
                return

    print('Проигрыш!')

field_of_dreams()