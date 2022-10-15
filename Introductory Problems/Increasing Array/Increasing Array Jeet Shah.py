n = int(input())
arr = list(map(int, input().split()))
count = 0
for a in range(len(arr)-1):
    if arr[a] > arr[a + 1]:
        count += (arr[a] - arr[a + 1])
        arr[a + 1] = arr[a]
print(count)
