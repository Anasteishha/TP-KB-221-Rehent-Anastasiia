def search_insert_position(sorted_list, target):
    left, right = 0, len(sorted_list) - 1

    while left <= right:
        mid = (left + right) // 2

        if sorted_list[mid] == target:
            return mid  # Знайдено точну позицію
        elif sorted_list[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return left  # Позиція для вставки нового елемента

# Приклад використання
sorted_list = [1, 3, 5, 6]
new_element = 4
position = search_insert_position(sorted_list, new_element)
print(f"Позиція для вставки {new_element}: {position}")
