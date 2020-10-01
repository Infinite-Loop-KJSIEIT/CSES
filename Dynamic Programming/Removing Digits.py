import sys
from itertools import permutations
def get_ints(): return map(int, sys.stdin.readline().strip().split())
n=int(input())
mod=10**9+7
dp=[10**9]*(n+1)
dp[0]=0
for i in range(1,n+1):
    for c in str(i):
        l=i-ord(c)+48
       # print(i,l,c)
        if l>=0:
            dp[i]=min(dp[i],dp[l]+1)
#print(dp)
print(dp[n])
