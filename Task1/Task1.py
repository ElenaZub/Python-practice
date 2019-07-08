if __name__ == '__main__':
    check = False
    while check == False:
        print("Enter the number:")
        n = int(input())
        if n >= 2 and n <= 10:
            check = True 
    array = list(set(map(int, input().split())))
    array.sort(reverse = True)
    print(array[1])
    