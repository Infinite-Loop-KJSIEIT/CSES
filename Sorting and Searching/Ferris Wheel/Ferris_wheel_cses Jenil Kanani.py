n, x = map(int, input().split())
arr = sorted(list(map(int, input().split())))
s,e = 0, n - 1
c = 0
while (e - s) > 1 :
    if (arr[s] + arr[e]) <= x:
        s += 1 
    e -= 1
    c += 1
if (arr[s] + arr[e]) <= x:
    c += 1
else:
    c+=2
print(c)

