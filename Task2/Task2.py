def second_min_value(items, second_min):
    min = second_min[1]
    for x in items:
        if(min == x[1]):
            second_min.append(items)  
            print(x[1])
    return second_min


if __name__ == '__main__':
    print("Enter number of students")
    students_result = []
    for x in range(int(input())):
        name = input()
        score = float(input())
        students_result.append([name, score])
    print("Students result:")    
    print(students_result)
    students_result.sort(key = lambda item : item[1])
    print(students_result)
    second_min = second_min_value(students_result, students_result[1])
    print(second_min)

   

    