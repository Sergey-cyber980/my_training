grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
def average(grades):
    obchaya_summa = sum(grades)
    return obchaya_summa / len(grades) if len(grades) else 0
result = {student: average(grade) for student, grade in zip(students, grades)}
print(result)
