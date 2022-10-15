N = int(input())
arr = list(map(int, input().split()))
arr.sort()
i = 0
while((i + 1) == arr[i]):
    i+=1 
    if i == N - 1:
        break 
print(i+1)