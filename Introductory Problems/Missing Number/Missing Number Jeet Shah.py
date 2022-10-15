n = int(input())
arr = list(map(int, input().split()))
target = (n * (n + 1)) // 2
real = sum(arr)
print(target - real)
