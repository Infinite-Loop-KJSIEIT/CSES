N = int(input())
arr1 = []
arr2 = []
for i in range(0,N - 6,8):
    arr1.append(1 + i)
    arr1.append(1 + i +1)
    arr1.append(7 + i)
    arr1.append(7+ i +1)
    arr2.append(3 + i)
    arr2.append(3 + i +1)
    arr2.append(5 + i)
    arr2.append(5+ i +1)

if N % 8 <= 4 and N % 8 > 0:
    if arr1:
        arr1.append(arr1[-1] + 1)
        arr1.append(arr1[-1] + 3)
        arr2.append(arr2[-1] + 4)
        arr2.append(arr2[-1] + 1)
    else:
        arr1.append(1)
        arr1.append(4)
        arr2.append(2)
        arr2.append(3)


if N % 4 == 1 or N % 4 == 2:
    print("NO")
elif N % 4 == 3:
    print("YES")
    print(int(N//2) + 1)
    if (N+1) % 16 == 0:
        arr1.remove(N + 1)
        arr1.append(arr2.pop(0))
        arr1.append(arr2.pop(((int((N + 1)/16) - 1) * 4)) + 1 )
    else:
        arr1.remove(N + 1)
        arr1.append(arr2.pop(arr2.index(int((N+1)//2))))
    print(*arr1)
    print(int(N/2))  
    print(*arr2)  

else:
    print("YES")
    print(int(N/2))
    print(*arr1)
    print(int(N/2))  
    print(*arr2)  

