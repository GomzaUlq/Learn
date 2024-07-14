def print_params(a=1, b='строка', c=True):
    print(a, b, c)


value_list = [4, 'слово', True ]
values_dict = {'a': 4, 'b': 'жизнь','c': False}
print_params(*value_list)
print_params(**values_dict)

values_list_2 = [54.32, 'Строка' ]
print_params(*values_list_2, 42)