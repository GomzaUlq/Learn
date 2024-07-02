grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
print(type(grades))
print(type(students))
first = sum(grades[0]) / len(grades[0])
print(first)
two = sum(grades[1]) / len(grades[1])
three = sum(grades[2]) / len(grades[2])
four = sum(grades[3]) / len(grades[3])
five = sum(grades[4]) / len(grades[4])
students_ = list (sorted(students))
solution = {(students_[0]) : float(first),(students_[1]) : float(two), (students_[2]) : float(three),(students_[3]) : float(four), (students_[4]) : float(five)}
print(solution)
