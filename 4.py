text = '''Тот, кого страшат шипы,
Не заполучит розы.'''

text = text.lower()

char_count = {}

for char in text:
    if char in char_count:
        char_count[char] += 1
    else:
        char_count[char] = 1

result = None
for char, count in char_count.items():
    if count == 3:
        result = char
        break

print(f'Символ, встречающийся ровно 3 раза: {result}')