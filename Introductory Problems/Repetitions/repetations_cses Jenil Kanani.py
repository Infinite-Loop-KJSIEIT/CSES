arr = input()
N = len(arr)
x = 0
i = 0
while(i < N - 1):
    j = 0
    while(arr[i + j] == arr[i + j + 1]):
        j+=1
        if (i + j + 1) == N:
            break
    j+=1
    if j > x:
        x = j
    i += j
if N == 1:
    print(1)
else:
    print(x)