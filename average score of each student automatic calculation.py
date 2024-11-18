grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
students_sorted = sorted(students)
students_sorted = list(students_sorted)
students_sorted_nuw = []
students_sorted_nuw[0] = (students_sorted[0]+':',(sum(grades[0])/len(grades[0])))
students_sorted_nuw[1] = (students_sorted[1]+':',(sum(grades[1])/len(grades[1])))
students_sorted_nuw[2] = (students_sorted[2]+':',(sum(grades[2])/len(grades[2])))
students_sorted_nuw[3] = (students_sorted[3]+':',(sum(grades[3])/len(grades[3])))
students_sorted_nuw[4] = (students_sorted[4]+':',(sum(grades[4])/len(grades[4])))

print(students_sorted_nuw)





#print(grades)
#print(students)
#Напишите программу, которая составляет словарь, используя grades и students, где ключом будет имя ученика, а значением - его средний балл.
#Otvet = zip(students_sorted,grades)
#print(list(Otvet))



