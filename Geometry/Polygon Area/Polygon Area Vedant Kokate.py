x=[]
y=[]
n=int(input())
for _ in range(n):
    a,b=map(int,input().split())
    x.append(a)
    y.append(b)
ans=0
for i in range(n-1):
    ans+=x[i]*y[i+1]-y[i]*x[i+1]
ans+=x[n-1]*y[0]-x[0]*y[n-1]
print(abs(ans))
    