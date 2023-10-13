def calculate_discriminant(A, B, C):
    return B**2 - 4*A*C

def find_roots(A, B, C):
    discriminant = calculate_discriminant(A, B, C)

    if discriminant > 0:
        # Два різних корені
        x1 = (-B + discriminant**0.5) / (2*A)
        x2 = (-B - discriminant**0.5) / (2*A)
        return x1, x2
    elif discriminant == 0:
        # Один подвійний корінь
        x = -B / (2*A)
        return x,
    else:
        # Немає дійсних коренів
        return None

# Приклад використання функції для знаходження коренів рівняння
A = 1
B = -3
C = 2

roots = find_roots(A, B, C)
if roots is not None:
    print("Корені рівняння:", roots)
else:
    print("Рівняння не має дійсних коренів.")
