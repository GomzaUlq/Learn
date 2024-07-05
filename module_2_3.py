my_list = [42, 69, 0, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
number = len(my_list)
a = 0
while a <= number :
    b = my_list[a]
    a = a + 1
    if b > 0:
        print (b)
        continue
    if b < 0 :
        break
