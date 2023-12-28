import csv

file_path = "students.txt"

while True:
    # Введення імені та оцінки
    name = input("Введіть ім'я студента (або 'e' для завершення): ")
    
    # Перевірка на вихід
    if name.lower() == 'e':
        break
    
    mark = input("Введіть оцінку студента: ")
    
    # Запис у файл
    with open(file_path, "a", newline='') as file:
        writer = csv.writer(file)
        writer.writerow([name, mark])

print("Дані збережено у файлі.")
