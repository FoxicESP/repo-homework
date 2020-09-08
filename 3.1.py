def div(*args):
    try:
        arg1 = int(input("Введите число "))
        arg2 = int(input("Введите число для деления "))
        res = arg1 / arg2
    except ValueError:
        return 'Ошибка, неправильное значение'
    except ZeroDivisionError:
        return "Неправильный делитель! Ноль нельзя использовать как делитель !"

    return res

print(f'Результат  {div()}')
