N = int(input())
arr = list(map(int, input().split()))
arr.sort()
x = arr[0]
c = 1
for i in range(1, len(arr)):
    if x != arr[i]:
        c += 1
        x = arr[i]
print(c)
