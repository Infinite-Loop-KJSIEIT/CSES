import sys
from collections import defaultdict
input=sys.stdin.readline
n,x=map(int,input().split())
a=list(map(int,input().split()))
dp=defaultdict(lambda : 0)
dp[0]+=1
count=0
sum=0
for i in a:
    sum+=i
    
    if sum-x in dp.keys():
        #print(sum)
        count+=dp[sum-x]
    dp[sum]+=1
print(count)
        
        
    



