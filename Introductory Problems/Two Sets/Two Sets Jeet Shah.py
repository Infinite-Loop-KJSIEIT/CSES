n = int(input())
pro = (n)*(n+1)//2
if pro % 2 != 0:
    print('NO')
else:
    arr1 = []
    arr2 = []
    j = n
    if (n % 2 == 0):
        i = 1
    else:
        arr1.append(1)
        arr1.append(2)
        arr2.append(3)
        i = 4
    while (i <= j):
        arr1.append(i)
        i += 1
        arr2.append(i)
        i += 1
        arr1.append(j)
        j -= 1
        arr2.append(j)
        j -= 1
    print('YES')
    print(len(arr1))
    for a1 in arr1:
        print(a1, end=" ")
    print()
    print(len(arr2))
    for a2 in arr2:
        print(a2, end=" ")
    print()
