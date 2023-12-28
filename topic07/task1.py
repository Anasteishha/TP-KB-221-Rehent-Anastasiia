class Student:
    def __init__(self, name, mark):
        self.name = name
        self.mark = mark

    def __str__(self):
        return f"Ім'я: {self.name}, Оцінка: {self.mark}"

# Використання
student1 = Student("Ana", 90)
print(str(student1))
