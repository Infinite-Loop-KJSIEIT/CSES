n = int(input())
c = 0
arr = list(map(int, input().split(' ')[:n]))
for i in range(0, n-1):
    if arr[i] > arr[i+1]:
        c = c + (arr[i]-arr[i+1])
        arr[i+1] = arr[i]
print(c)

