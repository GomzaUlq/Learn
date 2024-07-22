def calculate_structure_sum(*data):
    result = 0
    for i in data:
        if isinstance(i, str):
            result += len(i)
        elif isinstance(i, (list, tuple, set)):
            for j in i:
                result += calculate_structure_sum(j)
        elif isinstance(i, dict):
            for key, value in i.items():
                result += calculate_structure_sum(key, value)
        elif isinstance(i, int):
            result += i
    return result

data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]
result = calculate_structure_sum(data_structure)
print(result)
