n, m, k = map(int, input().split())
a = sorted(list(map(int, input().split())))
b = sorted(list(map(int, input().split())))
count = 0
i, j = 0, 0
while (i < n and j < m):
    if a[i] - k > b[j]:
        j += 1
    elif a[i] + k < b[j]:
        i += 1
    else:
        i += 1
        j += 1
        count += 1

print(count)
