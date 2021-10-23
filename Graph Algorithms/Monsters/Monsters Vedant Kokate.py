import time
import math
import sys
from collections import deque
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
q=deque()
step=[[0 for i in range(m)]for j in range(n)]
for i in range(n):
    for j in range(m):
        if a[i][j]=='A':
            sx=i
            sy=j
        if a[i][j]=='M':
            a[i][j]='#'
            q.append((i,j))
D=((0,1,'R'),(0,-1,'L'),(1,0,'D'),(-1,0,'U'))
R={'L':(0,1),'R':(0,-1),'D':(-1,0),'U':(1,0)}
while q:
    x,y=q.popleft()
    for r,c,d in D:
        X,Y=x+r,y+c
        if 0<=X<n and 0<=Y<m and a[X][Y]!='#' and step[X][Y]==0:
            step[X][Y]=step[x][y]+1
            q.append((X,Y))

q.append((sx,sy))
step[sx][sy]=0
a[sx][sy]='#'

while q:
    x,y=q.popleft()
    if x==0 or x==n-1 or y==0 or y==m-1:
        ans=[]
        while x!=sx or y!=sy:            
            ans.append(a[x][y])
            x1,y1=R[a[x][y]]
            x+=x1
            y+=y1
        
        print('YES')
        print(len(ans))
        print(''.join(reversed(ans)))
        raise SystemExit
    for r,c,d in D:
        X,Y=x+r,y+c
        if 0<=X<n and 0<=Y<m and a[X][Y]!='#' and (step[X][Y]==0 or step[X][Y]>step[x][y]+1):
            step[X][Y]=step[x][y]+1
            a[X][Y]=d
            q.append((X,Y))
print("NO")
 

