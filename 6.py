sentence = 'Любви, надежды, тихой славы недолго тешил нас обман.'

words = sentence.split()
reversed_words = words[::-1]

result = ' '.join(reversed(words))

print(f'Исходное предложение: {sentence}')
print(f'Предложение в обратном порядке слов: {result}')