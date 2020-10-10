import sys
from itertools import permutations
def get_ints(): return map(int, sys.stdin.readline().strip().split())
n,target=get_ints()
mod=10**9+7
c=list(get_ints())
dp=[0]*(target+1)
dp[0]=1
for i in range(1,target+1):
    for j in c:
        if i-j>=0:
            dp[i]+=dp[i-j]
            dp[i]%=mod

print(dp[target])
