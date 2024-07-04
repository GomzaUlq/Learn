name = print("Введите 3 числа по очереди: ")
first = int(input('1 : '))
second = int(input('2 : '))
third = int(input('3 : '))
if first == second == third:
    print('3')
elif first == second or first == third or second == third :
    print('2')
elif not first == second == third:
    print('0')
