def test_list_functions():
    # Початковий список
    my_list = [1, 2, 3]

    # Тест функції extend()
    my_list.extend([4, 5, 6])
    print("extend() результат:", my_list)

    # Тест функції append()
    my_list.append(7)
    print("append() результат:", my_list)

    # Тест функції insert()
    my_list.insert(1, 8)
    print("insert() результат:", my_list)

    # Тест функції remove()
    my_list.remove(3)
    print("remove() результат:", my_list)

    # Тест функції clear()
    my_list.clear()
    print("clear() результат:", my_list)

    # Повторно заповнимо список
    my_list = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    
    # Тест функції sort()
    my_list.sort()
    print("sort() результат:", my_list)

    # Тест функції reverse()
    my_list.reverse()
    print("reverse() результат:", my_list)

    # Тест функції copy()
    copied_list = my_list.copy()
    print("copy() результат:", copied_list)

# Виклик функції для тестування
test_list_functions()
