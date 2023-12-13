import logging
from operations import get_user_input, choose_operation
from functions import add, subtract, multiply, divide

logs = []

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

        class Logs():
            def __init__(self, number_1, number_2, operation, result):
                self.task = f'{number_1} {operation} {number_2} = {result}'
                logs.append(self.task)

        log = Logs(num1, num2, choice, result)

        ext = input('Натисніть E для виходу або log для перегляду логів: ')

        if ext == 'E':
            exit()
        elif ext == 'log':
            print('\n')
            for i in logs:
                print(i)

# Викликаємо головну функцію калькулятора
calculator()
