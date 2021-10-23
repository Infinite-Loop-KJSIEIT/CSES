N = int(input())
y = list(map(int, input().split()))
print(sum([i for i in range(1,N+1)])-sum(y))