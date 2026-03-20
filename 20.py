def number_to_words(n):
    ones = ['', 'один', 'два', 'три', 'четыре', 'пять', 'шесть',
            'семь', 'восемь', 'девять', 'десять', 'одиннадцать',
            'двенадцать', 'тринадцать', 'четырнадцать', 'пятнадцать',
            'шестнадцать', 'семнадцать', 'восемнадцать', 'девятнадцать'
    ]

    tens = ['', '', 'двадцать', 'тридцать', 'сорок', 'пятьдесят',
            'шестьдесят', 'семьдесят', 'восемьдесят', 'девяносто'
    ]

    hundreds = ['', 'сто', 'двести', 'триста', 'четыреста', 'пятьсот',
                'шестьсот', 'семьсот', 'восемьсот', 'девятьсот'
    ]

    def convert_hundreds(num):
        if num == 0:
            return ''
        if num < 20:
            return ones[num]
        if num < 100:
            return tens[num // 10] + (' ' + ones[num % 10] if
                                      num % 10 != 0 else '')
        return hundreds[num // 100] + (' ' + convert_hundreds(num % 100)
                                     if num % 100 != 0 else '')

    def convert_group(num, one, two, five):
        if num == 0:
            return ''
        if num == 1:
            return one
        elif 2 <= num <= 4:
            return two
        else:
            return five

    if n == 0:
        return 'ноль'

    words = []
    million = n // 1000000
    thousand = (n % 1000000) // 1000
    hundred = n % 1000

    if million > 0:
        words.append(convert_hundreds(million) + ' ' +
                     convert_group(million % 100 if 11 <= million % 100 <= 19
                                   else million % 10,
                                   'миллион', 'миллиона', 'миллионов'))

    if thousand > 0:
        words.append(convert_hundreds(thousand) + ' ' +
                     convert_group(thousand % 100 if 11 <= thousand % 100 <= 19
                                   else thousand % 10,
                                   'тысяча', 'тысячи', 'тысяч'))

    if hundred > 0:
        words.append(convert_hundreds(hundred))

    return ' '.join(words)

number = int(input('Введите число: '))
print(number_to_words(number))
