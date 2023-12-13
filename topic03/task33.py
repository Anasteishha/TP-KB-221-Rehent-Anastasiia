def test_dict_functions():
    # Початковий словник
    my_dict = {'a': 1, 'b': 2, 'c': 3}

    # Тест функції update()
    my_dict.update({'d': 4, 'e': 5})
    print("update() результат:", my_dict)

    # Тест функції del()
    del my_dict['b']
    print("del() результат:", my_dict)

    # Тест функції clear()
    my_dict.clear()
    print("clear() результат:", my_dict)

    # Повторно заповнимо словник
    my_dict = {'apple': 2, 'banana': 5, 'orange': 8}
    
    # Тест функції keys()
    keys = my_dict.keys()
    print("keys() результат:", keys)

    # Тест функції values()
    values = my_dict.values()
    print("values() результат:", values)

    # Тест функції items()
    items = my_dict.items()
    print("items() результат:", items)

# Виклик функції для тестування
test_dict_functions()
