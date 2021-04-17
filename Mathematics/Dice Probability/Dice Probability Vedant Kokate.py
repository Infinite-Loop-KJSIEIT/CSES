import sys 
input=sys.stdin.readline
n,a,b=map(int,input().split())
dp=[[0 for i in range(6*n+1)]for j in range(n+1)]
dp[0][0]=1
for i in range(1,n+1):
    for j in range(1,6*n+1):
        for k in range(1,7):
            if j-k>=0:
                dp[i][j]+=dp[i-1][j-k]
        dp[i][j]/=6
    # print(dp[i])
    # print(dp,i)

           
# print(dp)
x=sum(dp[n][i] for i in range(a,b+1))
print('{0:.{1}f}'.format(x, 6))