n = int(input())
lst = []
for _ in range(n):
    inp = tuple(map(int,input().split()))
    lst.append(inp)
lst.sort(key=lambda t: t[1])
print(lst)

prevfin = maxx = 0

for start, fin in lst:
    if prevfin <= start:
        maxx += 1
        prevfin = fin

print(maxx)