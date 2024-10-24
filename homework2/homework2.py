number = input("Введите десятичное число: ")

try:
    number = float(number)
except ValueError:
    print("Ошибка: Введено нечисловое значение.")
else:
    binary = bin(int(number))[2:] + ('.' + ''.join(str(int((number % 1) * 2 ** i) % 2) for i in range(1, 11)) if number % 1 else '')
    octal = oct(int(number))[2:] + ('.' + ''.join(str(int((number % 1) * 8 ** i) % 8) for i in range(1, 11)) if number % 1 else '')
    
    print("Двоичное представление:", binary)
    print("Восьмеричное представление:", octal)
