import sys
input=sys.stdin.readline
n=int(input())
a=[]
for i in range(n):
    x,y=map(int,input().split())
    a.append((x,y,i))
a.sort(key=lambda x:(x[0],-x[1]))
# print(a)
max_R=-1
min_L=10**10
ans1=['0']*n
ans2=['0']*n
for i in range(n):
    if a[i][1]<=max_R:
        ans2[a[i][2]]='1'
    else:
        max_R=a[i][1]
    if a[n-1-i][1]>=min_L:
        ans1[a[n-1-i][2]]='1'
    else:
        min_L=a[n-1-i][1]
 
 
print(" ".join(ans1))
print(" ".join(ans2))