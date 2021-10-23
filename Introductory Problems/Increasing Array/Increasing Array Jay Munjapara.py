n = int(input())
l = list(map(int, input().split()))
i, x = 0, []
while i < n-1: 
    if (l[i+1] < l[i]):
        x.append(abs(l[i+1] - l[i]))
        l[i+1] += abs(l[i+1] - l[i])
    i += 1
print(sum(x))