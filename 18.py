main_text = '''Научный мир удивителен и бескраен. Мы постоянно открываем
что-то новое, иследуем тайны Вселенной и пытаемся понять её законы.
Кажется, что человеческие знания не ограничны, и мы способны постигнуть
всё, что угодно. Но реальность всегда оказывается сложнее предположений,
поэтому знания важно не только накапливать, но и учиться их применять,
чтобы менять мир к лучшему.
'''

def justify_text(text, line_width):
    words = text.split()
    lines = []
    current_line = []

    for word in words:
        if (sum(len(w) for w in current_line) + len(word)
                    + len(current_line) - 1 < line_width):
            current_line.append(word)
        else:
            lines.append(current_line)
            current_line = [word]

    if current_line:
        lines.append(current_line)

    justified_lines = []
    for line in lines[:-1]:
        total_spaces = line_width - sum(len(word) for word in line)
        if len(line) > 1:
            spaces_between = total_spaces // (len(line) - 1)
            extra_spaces = total_spaces % (len(line) - 1)
            justified_line = ''
            for i, word in enumerate(line):
                justified_line += word
                if i < len(line) - 1:
                    justified_line += ' ' * (spaces_between
                          + (1 if i < extra_spaces else 0))
            justified_lines.append(justified_line)
        else:
            justified_lines.append(line[0] + ' ' * total_spaces)

    justified_lines.append(' '.join(lines[-1]))

    return '\n'.join(justified_lines)

max_length = 40

print(justify_text(main_text, max_length))