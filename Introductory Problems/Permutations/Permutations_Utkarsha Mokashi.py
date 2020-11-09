n = int(input())
j = n-1
a = n
k = int(n/2)
arr = []
if n > 3:
    for i in range(0, k):
        arr.append(j)
        j = j - 2
    for i in range(k, n):
        arr.append(a)
        a = a - 2
    for i in arr:
        print(i, end=" ")
else:
    if n == 1:
        print("1")
    else:
        print("NO SOLUTION")
 