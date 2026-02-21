text = '''Когда так много позади
          Всего, в особенности - горя,
          Поддержки чьей-нибудь не жди,
          Сядь в поезд, высадись у моря.'''

max_spaces = 0
current_spaces = 0

for char in text:
    if char == ' ':
        current_spaces += 1
        max_spaces = max(max_spaces, current_spaces)
    else:
        current_spaces = 0

print(f'Максимальное количество последовательных пробелов: {max_spaces}')