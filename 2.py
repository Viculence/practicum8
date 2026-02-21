text = '''Какая ночь! Я не могу.
Не спится мне. Такая лунность.
Ещё как будто берегу
В душе утраченную юность.'''

if len(text) == 0:
    print('Строка пустая')
else:
    max_count =1
    current_count = 1

    for i in range(1, len(text)):
        if text[i] == text[i-1]:
            current_count += 1
            max_count = max(max_count, current_count)
        else:
            current_count = 1

    print(f'Максимальное количество последовательных'
          f' одинаковых символов: {max_count}'
    )