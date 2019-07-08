def avarage_mark(marks: list) -> float:
    return sum(marks)/len(marks)


def query_marks(students: dict, student_name: str) -> list:
    return students.get(student_name)


if __name__ == '__main__':
    student_marks = {}
    
    for _ in range(int(input())):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores

    student_marks = query_marks(students=student_marks, student_name=input())
    print("{0:.2f}".format(avarage_mark(student_marks)))
