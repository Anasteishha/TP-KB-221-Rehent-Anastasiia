import logging
import os
from operations import get_user_input, choose_operation
from functions import add, subtract, multiply, divide

# Отримання поточного каталогу
current_directory = os.getcwd()

# Ім'я файлу логів
log_file = os.path.join(current_directory, 'calc_log.txt')

# Налаштування логування
logging.basicConfig(filename=log_file, level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

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

        # Логування в файл
        with open(log_file, 'a') as log:
            log.write(f'Введені дані:    {num1} та {num2}\n')
            log.write(f'Обрана операція: {choice}\n')
            log.write(f'Результат:       {result}\n')
            log.write(f'{num1} {choice} {num2} = {result}\n\n')

        ext = input('Type E to exit: ')
        if ext == 'E':
            exit()

# Викликаємо головну функцію калькулятора
calculator()
