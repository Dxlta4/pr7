def decimal_to_base13(decimal_number):
    digits = '0123456789ABC'
    
    if decimal_number == 0:
        return '0'
    
    sign = '-' if decimal_number < 0 else ''
    
    decimal_number = abs(decimal_number)
    
    integer_part = int(decimal_number)
    base13_integer = convert_integer_to_base13(integer_part, digits)
    
    fractional_part = decimal_number - integer_part
    base13_fraction = convert_fraction_to_base13(fractional_part, digits) if fractional_part > 0 else ''
    
    return sign + base13_integer + ('.' + base13_fraction if base13_fraction else '')

def convert_integer_to_base13(n, digits):
    if n == 0:
        return ''
    else:
        return convert_integer_to_base13(n // 13, digits) + digits[n % 13]

def convert_fraction_to_base13(fraction, digits, precision=5):
    if precision == 0 or fraction == 0:
        return ''
    fraction *= 13
    digit = int(fraction)
    return digits[digit] + convert_fraction_to_base13(fraction - digit, digits, precision - 1)

def is_valid_input(user_input):
    try:
        float(user_input)
        return True
    except ValueError:
        return False

user_input = input("Введите десятичное число: ")

if is_valid_input(user_input):
    decimal_number = float(user_input)
    print(f"Число {decimal_number} в тринадцатеричной системе счисления: {decimal_to_base13(decimal_number)}")
else:
    print("Ошибка: Введите корректное десятичное число.")
