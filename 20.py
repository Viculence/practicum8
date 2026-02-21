def number_to_words(n):
    ones = ['', 'один', 'два', 'три', 'четыре', 'пять', 'шесть',
            'семь', 'восемь', 'девять', 'десять', 'одиннадцать',
            'двенадцать', 'тринадцать', 'четырнадцать', 'пятнадцать',
            'шестнадцать', 'семнадцать', 'восемьнадцать', 'девятнадцать'
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
                                      num % 10 != 0 else ''
            )
        return hundreds[num // 100] + (' ' + convert_hundreds(num % 100)
                                     if num % 100 != 0 else ''
        )


    def convert_thousands(num):
        if num == 0:
            return ''
        if num == 1:
            return 'тысяча'
        elif 2 <= num <= 4:
            return 'тысячи'
        else:
            return 'тысяч'

    if n == 0:
        return 'ноль'

    words = []
    billion = n // 1000000000
    million = (n % 1000000000) // 1000000
    thousand = (n % 1000000) // 1000
    hundred = n % 1000

    if billion > 0:
        words.append(convert_hundreds(billion) + 'миллиардов')

    if million > 0:
        words.append(convert_hundreds(million) + 'миллионов')

    if thousand > 0:
        words.append(convert_hundreds(thousand) + ' ' +
                     convert_thousands(thousand)
        )

    if hundred > 0:
        words.append(convert_hundreds(hundred))

    return ' '.join(words)

number = int(input('Введите число: '))

print(number_to_words(number))