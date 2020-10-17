import time
import math
import sys 
def get_ints(): return map(int, sys.stdin.readline().strip().split())
def ipi(): return int(sys.stdin.readline().strip())
def ips(): return(sys.stdin.readline().strip())
sys.setrecursionlimit(10**6)
    #Initialize a queue
 
 
 
n,m=get_ints()
a=[]
for i in range(n):
    s=ips()
    l=[]
    l[:0]=s    
    a.append(l)
 
step=[["" for i in range(m)]for j in range(n)]
step2=[["" for i in range(m)]for j in range(n)]
vis=[[True for i in range(m)]for j in range(n)]
sx=sy=0
q=[]
for i in range(n):
    for j in range(m):
        if a[i][j]=='A':
            sx=i
            sy=j
        if a[i][j]=='M':
            q.append([i,j])
            vis[i][j]=False
r=[0,0,1,-1]
c=[1,-1,0,0]
d=['R','L','D','U']
 
while q:
   # print(q)
    s=q.pop(0)
    x1=s[0]
    y1=s[1]
    for i in range(4):
        x=x1+r[i]
        y=y1+c[i]
        #print(x,y)
        if x<n and x>-1 and y<m and y>-1 and a[x][y]!='#' and vis[x][y]:
            vis[x][y]=False
            q.append([x,y])
            step[x][y]=str(step[x1][y1])+d[i]
q.append([sx,sy])
flag=False
while q:
    #print(q)
    s=q.pop(0)
    x1=s[0]
    y1=s[1]
    if x1==0 or y1==0 or x1==n-1 or y1==m-1:
        print("YES")
        print(len(step2[x1][y1]))
        print(step2[x1][y1])
        flag=True
        break
    
    for i in range(4):
        
        x=x1+r[i]
        y=y1+c[i]
       # print(x,y)
        if x<n and x>-1 and y<m and y>-1 and a[x][y]=='.' :
            step2[x][y]=step2[x1][y1]+d[i]
            a[x][y]='#'
            if len(step2[x][y])>=len(step[x][y]) and len(step[x][y])!=0:
                continue
            q.append([x,y])
if not flag:
    print("NO")
 
'''for i in step2:
    print(i)
 
for i in step:
    print(i)'''
                
