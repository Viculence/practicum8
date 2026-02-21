sentence = 'Ты у звезды учись тому, что значит свет.'

words = sentence.split()

if words:
    min_length = min(len(word) for word in words)
    shortest_word = [word for word in words if len(word) == min_length]

    print(f'Самое короткое слово: {shortest_word}')
    print(f'Длина самого короткого слова: {min_length}')
else:
    print('Предллжение пустое')