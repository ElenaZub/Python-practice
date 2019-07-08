students = [[input(), float(input())] for _ in range(int(input()))]
students_sorted = (sorted(list(set([mark for name, mark in students]))))
second_lowest_grade_students = [name for name, mark in students if mark == students_sorted[1]]
for item in second_lowest_grade_students:
    print(item)
