n = int(input())
if n == 1:
    print(1)
if n == 4:
    print('2 4 1 3')
elif n >= 5:
    for i in range(0, n, 2):
        print(i+1, end=' ')
    for j in range(1, n, 2):
        print(j+1, end=' ')
else:
    print('NO SOLUTION')
