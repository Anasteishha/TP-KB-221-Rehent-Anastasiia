from functions import add, subtract, multiply, divide

# Функція для отримання вводу від користувача
def get_user_input():
    num1 = float(input("Введіть перше число: "))
    num2 = float(input("Введіть друге число: "))
    return num1, num2

# Функція для вибору операції
def choose_operation():
    print("Оберіть операцію:")
    print("1. Додавання")
    print("2. Віднімання")
    print("3. Множення")
    print("4. Ділення")
    print("5. Вихід")
    choice = input("Введіть номер операції (1/2/3/4/5): ")
    return choice
