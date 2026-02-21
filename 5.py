str1 = 'Я помню чудное мгновенье'
str2 = 'Передо мной явилась ты'
str3 = 'Как мимолётное виденье'

only1 = set(str1.lower()) - set(str2.lower()) - set(str3.lower())
only2 = set(str2.lower()) - set(str1.lower()) - set(str3.lower())
only3 = set(str3.lower()) - set(str1.lower()) - set(str2.lower())

unique_chars = {
    char for char in (only1 | only2 | only3)
    if char.isalpha()
}

print(f'Все символы, встречающиеся только в 1 строке:\n'
      f'{sorted(unique_chars)}'
)
print(f'Только в 1-й строке: {sorted(c for c in only1 if c.isalpha())}')
print(f'Только во 2-й строке: {sorted(c for c in only2 if c.isalpha())}')
print(f'Только в 3-й строке: {sorted(c for c in only3 if c.isalpha())}')