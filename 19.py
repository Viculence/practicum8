main_text = '''Научный мир удивителен и бескраен. Мы постоянно открываем
что-то новое, иследуем тайны Вселенной и пытаемся понять её законы.
Кажется, что человеческие знания не ограничны, и мы способны постигнуть
всё, что угодно. Но реальность всегда оказывается сложнее предположений,
поэтому знания важно не только накапливать, но и учиться их применять,
чтобы менять мир к лучшему.
'''

VOWELS = 'аеёиоуыьъэюяАЕЁИОУЫЬЪЭЮЯ'
CONSONANTS = 'бвгджзйклмнпрстфхцчшщБВГДЖЗЙКЛМНПРСТФХЦЧШЩ'


# Находит позиции в слове, где можно сделать перенос по слогам
# Возвращает список индексов символов, после которых можно разделить слово
def get_syllable_breaks(word):
    breaks = []
    vowel_position = [i for i, c in enumerate(word) if c in VOWELS]

    if len(vowel_position) < 2:
        return []

    for k in range(len(vowel_position) - 1):
        v1 = vowel_position[k]
        v2 = vowel_position[k + 1]

        between = list(range(v1 + 1, v2))
        consonants_between = [i for i in between if word[i] in CONSONANTS]

        if not consonants_between:
            break_pos = v1 + 1
        elif len(consonants_between) == 1:
            break_pos = consonants_between[0]
        else:
            if word[consonants_between[0]] == 'й':
                break_pos = consonants_between[1]
            else:
                break_pos = consonants_between[1]

        part1 = word[:break_pos]
        part2 = word[break_pos:]
        letters1 = sum(1 for c in part1 if c.isalpha())
        letters2 = sum(1 for c in part2 if c.isalpha())

        if letters1 >= 2 and letters2 >= 2:
            breaks.append(break_pos)

    return breaks


# Разделяет слово на две части с переносом по слогам
# Первая часть (с дефисом) должна поместиться в max_len символов
# Возвращает кортеж (часть1_с_дефисом, часть2) или None если не удалось
def split_word_for_fit(word, max_len):
    suffix = ''
    core = word
    while core and not core[-1].isalpha():
        suffix = core[-1] + suffix
        core = core[:-1]

    breaks = get_syllable_breaks(word)

    for bp in reversed(breaks):
        part1 = core[:bp] + '-'
        part2 = core[bp:] + suffix
        if len(part1) <= max_len:
            return part1, part2

    return None


# Форматирует текст в колонку заданной ширины с выравниванием по ширине
# Переносит слова по слогам и равномерно распределяет пробелы между словами
def justify_text(text, line_width):
    words = text.split()
    lines = []
    current_line = []

    i = 0
    while i < len(words):
        word = words[i]

        fits = (sum(len(w) for w in current_line) + len(word)
                + (len(current_line) if current_line else 0)) <= line_width

        if fits:
            current_line.append(word)
            i += 1
        else:
            used = sum(len(w) for w in current_line) + len(current_line)
            available = line_width - used

            split = None
            if available >= 3:
                split = split_word_for_fit(word, available)

            if split:
                part1, part2 = split
                current_line.append(part1)
                lines.append(current_line)
                current_line = [part2]
                i += 1
            else:
                if current_line:
                    lines.append(current_line)
                    current_line = [word]
                    i += 1
                else:
                    current_line.append(word)
                    i += 1

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
