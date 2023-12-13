from operations import get_user_input, choose_operation
from functions import add, subtract, multiply, divide

# Головна функція калькулятора
def calculator():
    while True:
        choice = choose_operation()

        if choice == '5':
            print("Дякуємо за використання калькулятора. До побачення!")
            break

        num1, num2 = get_user_input()

        if choice == '1':
            result = add(num1, num2)
        elif choice == '2':
            result = subtract(num1, num2)
        elif choice == '3':
            result = multiply(num1, num2)
        elif choice == '4':
            result = divide(num1, num2)
        else:
            result = "Неправильний вибір операції"

        print("Результат:", result)

# Викликаємо головну функцію калькулятора
calculator()
