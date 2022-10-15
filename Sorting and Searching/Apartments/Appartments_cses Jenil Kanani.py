n, m , k = map(int, input().split())
req = sorted(list(map(int, input().split())))
avl = sorted(list(map(int, input().split())))
c,b  = 0, 0
for i in req:
    for j in range(b,m):
        if (i - k <= avl[j]) and (avl[j] <= i + k):
            c += 1
            b = j + 1
            break
        elif avl[j] > i + k:
            b = j
            break
        elif j == 0 and i - k > avl[-1]:
            break 
print(c)