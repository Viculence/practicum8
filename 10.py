sentence = '''Всё умирает на земле и в море,
Но человек суровей осуждён:
Он должен знать о смертном приговоре,
Подписанном, когда он был роджён.'''

words = sentence.split()

if words:
    word1 = words[0]

    result = []
    for word in words[1:]:
        if word != word1 and len(word) == len(set(word)):
            result.append(word)

    print(sentence)
    print('\nПервое слово:', word1)
    print(f'\nСлова, отличные от первого, без повторяющихся букв: \n'
          f'{result}'
    )