grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
students_grades = []
students_sorted = sorted(students)
students_grades.append((students_sorted[0],(sum(grades[0])/len(grades[0]))))
students_grades.append((students_sorted[1],(sum(grades[1])/len(grades[1]))))
students_grades.append((students_sorted[2],(sum(grades[2])/len(grades[2]))))
students_grades.append((students_sorted[3],(sum(grades[3])/len(grades[3]))))
students_grades.append((students_sorted[4],(sum(grades[4])/len(grades[4]))))
students_grades = dict(students_grades)
print(students_grades)



