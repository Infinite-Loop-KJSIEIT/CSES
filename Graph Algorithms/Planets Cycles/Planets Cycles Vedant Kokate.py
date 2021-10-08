import sys
input=sys.stdin.readline
sys.setrecursionlimit(10**6)
I=lambda:list(map(int,sys.stdin.readline().split()))


n = int(input())
a =[0,*I()] 
ans = [0]*(n+1)

vis = [False]*(n+1)
for i in range(1,n+1):
    if not vis[i]:
        vis[i]=True
        d={}
        value=0
        d[i]=value
        cur=a[i]
        stack=[i]

        while not vis[cur]:
            # print(d)
            stack.append(cur)
            vis[cur]=True
            value+=1
            # print('value',value,cur)
            d[cur]=value
            cur=a[cur]
            
        # print('value ',stack)
        if cur in d:
            # print('value 2',value)
            cycle_value = value-d[cur]+1
            # print(cycle_value,value)
            for j in range(d[cur],len(stack)):
                ans[stack[j]]= cycle_value
            # print(d)
            for j in range(d[cur]):
                ans[stack[j]] = cycle_value - j + d[cur]
        else:
            for j in range(len(stack)):
                ans[stack[j]] = len(stack) - j + ans[cur]


            # print(stack)
        # print(stack,vis,d)
print(*ans[1:])

