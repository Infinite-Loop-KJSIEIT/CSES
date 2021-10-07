import sys
input=sys.stdin.readline
sys.setrecursionlimit(10**6)
I=lambda:list(map(int,sys.stdin.readline().split()))


n,q=I()
dp=[[0,*I()]]
for i in range(31):
    temp=dp[-1]
    dp.append([temp[j] for j in temp])
# print(dp)

for _ in range(q):
    x,y=I()
    for i in range(31):
        if y&(1<<i):
            x=dp[i][x]
    print(x)

