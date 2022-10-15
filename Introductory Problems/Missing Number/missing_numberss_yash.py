n = int(input())
y = list (map(int,input().split()))
y=sorted(y)
print(int((n*(n+1))/2 - sum(y)))