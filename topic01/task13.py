def calculate_discriminant(A, B, C):
    return B**2 - 4*A*C

# Приклад використання функції для обчислення дискримінанту
A = 1
B = -3
C = 2

discriminant = calculate_discriminant(A, B, C)
print("Дискримінант:", discriminant)
