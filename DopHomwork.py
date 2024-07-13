numb =int(input())
password = ''
for first_number in range(1, numb):
    for second_number in range(first_number + 1, numb):
        if numb % (first_number + second_number) == 0:
            password += (str(first_number) + str(second_number))
print(password)
