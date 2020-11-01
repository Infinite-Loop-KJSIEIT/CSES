n = int(input())
if 1< n < 5:
    if n == 4:
        print("2 4 1 3")
    else:
        print("NO SOLUTION")
else:
    if n%2 != 0:
        h = (n // 2) + 1
    else:
        h = n // 2
    for i in range(1,(n // 2) + 1):
        print(i,h + i,end=" ")
    if n%2 != 0:
        print((n // 2) + 1,end=" ")