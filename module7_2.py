import io
from pprint import pprint


def custom_write(file_name, strings):
    string_positions = {}
    file = open(file_name, 'r+', encoding='utf-8')
    number = 1
    for line in strings:
        string_positions[(number, file.tell())] = line
        file.write(line + '\n')
        number += 1
    file.close()
    return string_positions


info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
]

result = custom_write('test.txt', info)
for elem in result.items():
    print(elem)
