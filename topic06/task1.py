import csv

students_data = []

# Замініть "students.txt" на шлях до вашого файлу з даними
with open("students.txt", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        students_data.append({"name": row["Name"], "mark": row["Mark"]})

# Сортування по оцінкам
print("Сортування по оцінкам:")
for student in sorted(students_data, key=lambda elem: elem['mark']):
    print(f"Ім'я: {student['name']}, Оцінка: {student['mark']}")

print('\n')

# Сортування по імені
print("Сортування по імені:")
for student in sorted(students_data, key=lambda elem: elem['name']):
    print(f"Ім'я: {student['name']}, Оцінка: {student['mark']}")

