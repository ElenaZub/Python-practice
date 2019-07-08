def list_second_min(items, second):
    second_list = []
    for x in items:
        if x[1] == second:
            second_list.append(x)
    return second_list


if __name__ == '__main__':
    students_result = []
    score_list = []
    for x in range(int(input())):
        name = input()
        score = float(input())
        score_list.append(score)
        students_result.append([name, score])
    second_min = (sorted(set(score_list)))[1]    
    #print(students_result)
    lowels_marks_list = list_second_min(students_result, second_min)
    #print(lowels_marks_list)
    lowels_marks_list.sort(key = lambda item: item[0])
    for x in lowels_marks_list:
        print(x[0])


    
