# Функція для додавання чисел
def add(x, y):
    return x + y

# Функція для віднімання чисел
def subtract(x, y):
    return x - y

# Функція для множення чисел
def multiply(x, y):
    return x * y

# Функція для ділення чисел
def divide(x, y):
    if y == 0:
        return "Ділення на нуль неможливе"
    return x / y

# Головна функція калькулятора
def calculator():
    print("Оберіть операцію:")
    print("1. Додавання")
    print("2. Віднімання")
    print("3. Множення")
    print("4. Ділення")

    choice = input("Введіть номер операції (1/2/3/4): ")

    num1 = float(input("Введіть перше число: "))
    num2 = float(input("Введіть друге число: "))

    if choice == '1':
        result = add(num1, num2)
        print("Результат додавання:", result)
    elif choice == '2':
        result = subtract(num1, num2)
        print("Результат віднімання:", result)
    elif choice == '3':
        result = multiply(num1, num2)
        print("Результат множення:", result)
    elif choice == '4':
        result = divide(num1, num2)
        print("Результат ділення:", result)
    else:
        print("Неправильний вибір операції")

# Викликаємо головну функцію калькулятора
calculator()
