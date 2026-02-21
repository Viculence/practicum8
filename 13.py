def happy_ticket(ticket_number):
    ticket_str = str(ticket_number)
    length = len(ticket_str)

    if length % 2 != 0:
        return False

    half1 = ticket_str[:length // 2]
    half2 = ticket_str[length // 2:]

    if sum(int(digit) for digit in half1) \
            == sum(int(digit) for digit in half2):
        return True
    return False


def ticket_cycle():
    count = 1
    while True:
        ticket_number = input('Введите номер билета: ')
        if happy_ticket(ticket_number):
            print(f'Счастливый билет! Его порядковый номер: {count}')
            break
        count += 1


ticket_cycle()