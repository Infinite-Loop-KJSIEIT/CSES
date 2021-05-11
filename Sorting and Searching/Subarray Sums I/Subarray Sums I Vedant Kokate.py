import sys
input=sys.stdin.readline
n,x=map(int,input().split())
a=list(map(int,input().split()))
dp={0:0}
count=0
sum=0
for i in a:
    sum+=i
    
    if sum-x in dp.keys():
        #print(sum)
        count+=1
    dp[sum]=1
print(count)
        
        
    



