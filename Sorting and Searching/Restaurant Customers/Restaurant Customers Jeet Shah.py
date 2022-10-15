n = int(input())
arr = []
dep = []
for _ in range(n):
    x, y = map(int, input().split())
    arr.append(x)
    dep.append(y)

arr.sort()
dep.sort()

i, j = 0, 0
mx = 0
cus = 0

while i < n and j < n:
    if arr[i] < dep[j]:
        cus += 1
        i += 1
    else:
        j += 1
        cus -= 1
    if mx < cus:
        mx = cus

print(mx)
