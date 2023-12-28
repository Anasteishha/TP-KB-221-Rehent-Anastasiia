import csv

names = []

class Student:
    def __init__(self, name, age):
        self.name = name 
        self.age = age

        names.append({"name": name, "age": age})

stud1 = Student('Ana', 18)
stud2 = Student('Mark', 20)
stud3 = Student('Maria', 19)
stud4 = Student('Alexa', 21)
stud5 = Student('Alina', 25)
stud6 = Student('Lina', 23)
# Сортування по віку
for name in sorted(names, key=lambda elem: elem['age']):
    print(f"Your name is {name['name']} your age is {name['age']}")

print('\n')

# Сортування по імені
for name in sorted(names, key=lambda elem: elem['name']):
    print(f"Your name is {name['name']} your age is {name['age']}")
