sentence = 'Товарищ, верь: взойдет она, звезда пленительного счастья.'

words = sentence.split()

sorted_words = sorted(words, key=len)

print(f'Исходное предложение: {sentence}')
print(f'Слова в порядке неубывания длин: {sorted_words}')