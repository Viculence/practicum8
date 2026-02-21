sentence = '''Кому-то мелочь дашь, навек запомнит,
Кому-то жизнь отдашь, а он и не поймёт.'''

words = sentence.split()

word_count = {}
for word in words:
    word_count[word] = word_count.get(word, 0) + 1

copy_words = [word for word, count in word_count.items() if count > 1]

print(sentence)
print(f'Повторяющееся слово: {copy_words}')