def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Ошибка: введите число.")

def solve_equation(a, b, c):
    return 7 * b + 2 * c - a

# Ввод данных с проверкой
a = get_number("Введите значение a: ")
b = get_number("Введите значение b: ")
c = get_number("Введите значение c: ")

# Решение уравнения
x = solve_equation(a, b, c)
print(f"Результат: x = {x}")
