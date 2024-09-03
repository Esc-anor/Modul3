# Создаём функцию подсчёта данных строк и чисел
def calculate_structure_sum(data_structure):
    sum = 0
    # Прописываем условие при помощи цикла 1 sum для словаря
    if isinstance(data_structure, dict):
        for key, value in data_structure.items():
            sum += calculate_structure_sum(key)
            sum += calculate_structure_sum(value)
            # иначе выполняется цикл 2 добавление к sum - список, кортэж, множества
    elif isinstance(data_structure, (list, tuple, set)):
        for item in data_structure:
            sum += calculate_structure_sum(item)
            # иначе выполняется действие 3 добавление к sum - целое число и число с плавающей запятой
    elif isinstance(data_structure, (int, float)):
        sum += data_structure
        # иначе выполняется действие 4 добавление k sum - функцию len
    elif isinstance(data_structure, str):
        sum += len(data_structure)
        # возврат из функции значения summa
    return sum


# данные взятые из условия задачи
data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]
# вывод результата программы
result = calculate_structure_sum(data_structure)
print(result)
