import keyword

def valid_variable_name(name):
    if name.isidentifier() and name not in keyword.kwlist:
        return "Допустимое имя переменной"
    else:
        return "Недопустимое имя переменной"

input_name = input("Введите имя переменной: ")
print(valid_variable_name(input_name))
