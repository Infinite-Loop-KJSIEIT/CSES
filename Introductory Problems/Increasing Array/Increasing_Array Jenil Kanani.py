N = int(input())
arr = list(map(int, input().split()))
i, count = 0, 0
while(i < N - 1):
    if arr[i] > arr[i + 1]:
        count += (arr[i] - arr[i + 1])
        arr[i + 1] = arr[i]
    i += 1
print(count)