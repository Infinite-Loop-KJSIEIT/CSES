n = int(input())
arr=list(map(int, input().split(' ')[:n-1]))
s1 = (n*(n+1))/2;
s=0
for i in range(n-1):
    s = s + arr[i]
print(int(s1 - s))





