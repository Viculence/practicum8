text = '''Смотрю на море жадными очами,
К земле прикованный, на берегу.
Стою над пропастью - над небесами, -
И улететь к лазури не могу.'''

different_letters = set()

for char in text.lower():
    if char.isalpha():
        different_letters.add(char)

print(f'Количество различных букв: {len(different_letters)}')
print(f'Буквы: {sorted(different_letters)}')