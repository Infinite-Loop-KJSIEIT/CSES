n = int(input())
x, y = [], []
for i in range(1,n+1):
    if i%2 == 0:
        x.append(i) 
    elif i%2 == 1:
        y.append(i)
z = x + y
l = [abs(z[m+1] - z[m]) for m in range(n-1)]
if 1 in l:
    print("NO SOLUTION")
else:
    print(*z)