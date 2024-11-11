grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
sorted_students = sorted(students)
average_scores = {}
for i, student in enumerate(sorted_students):
    student_grades = grades[i]
    average_score = sum(student_grades) / len(student_grades)
    average_scores[student] = average_score
print(average_scores)