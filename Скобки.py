def checked():
    str_input = input()
    str = []
    for i in str_input:
        if i == '(' or i == ')' or i == '[' or i == ']' or i == '{' or i == '}':
            str.append(i)
    j = 1
    count1 = len(str)
    count2 = 0
    while count1 != count2:
        count2 = count1
        while j < len(str):
            if str[j] == ')' and str[j - 1] == '(':
                str.pop(j)
                str.pop(j - 1)
                j -= 1
            elif str[j] == ']' and str[j - 1] == '[':
                str.pop(j)
                str.pop(j - 1)
                j -= 1
            elif str[j] == '}' and str[j - 1] == '{':
                str.pop(j)
                str.pop(j - 1)
                j -= 1
            else:
                j += 1
        count1 = len(str)
    if len(str) == 0:
        print('True')
    else:
        print("False")
    
checked()
def checked():
    arr_input = input()
    # arr_input = '1,1,2,2,3'
    arr = arr_input.split(',')
    arr = [int (x) for x in arr]
    a = int(input())
    b = int(input())
    c = int(input())
    # a = 0
    # b = 0
    # c = 1
    count = 0
    i = 0
    j = 0
    k = 0
    while i < len(arr):
        while j < len(arr):
            while k < len(arr):
                # print(i, j, k)
                if i < j and j < k:
                    if abs(arr[i] - arr[j]) < a and abs(arr[j] - arr[k]) < b and abs(arr[i] - arr[k]) < c:
                        count += 1
                k += 1
            k = 0
            j += 1
        j = 0
        i += 1
    print(count)

checked()