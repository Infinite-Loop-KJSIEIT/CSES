import time
import math
import sys 
def get_ints(): return map(int, sys.stdin.readline().strip().split())
def ipi(): return int(sys.stdin.readline().strip())
def ips(): return(sys.stdin.readline().strip())
sys.setrecursionlimit(10**6)
    #Initialize a queue
 
def bfs(vis, a, node):
    vis[str(node[0])+" "+str(node[1])]=1
    queue.append(node)
    path=[["" for i in range(m)]for j in range(n)]
    while queue:
       # print (queue,vis)
        s = queue.pop(0)
       
        x=s[0]
        y=s[1]
 
        if a[x][y]=='B':
            print("YES")
            print(len(path[x][y]))
            print(path[x][y])
            return
        if x+1<n and a[x+1][y]!='#' and str(x+1)+" "+str(y) not in vis.keys():
            st=str(x+1)+" "+str(y)
            vis[st]=1
            queue.append([x+1,y])
            path[x+1][y]=path[x][y]+"D"
        if x-1>-1 and a[x-1][y]!='#' and str(x-1)+" "+str(y) not in vis.keys():
            st=str(x-1)+" "+str(y)
            vis[st]=1
            queue.append([x-1,y])
            path[x-1][y]=path[x][y]+"U"
        if y+1<m and a[x][y+1]!='#' and str(x)+" "+str(y+1) not in vis.keys():
            st=str(x)+" "+str(y+1)
            vis[st]=1
            queue.append([x,y+1])
            path[x][y+1]=path[x][y]+"R"
        if y-1>-1 and a[x][y-1]!='#' and str(x)+" "+str(y-1) not in vis.keys():
            st=str(x)+" "+str(y-1)
            vis[st]=1
            queue.append([x,y-1])
            path[x][y-1]=path[x][y]+"L"
    print("NO")
 
        
 
n,m=get_ints()
a=[]
for i in range(n):
    s=ips()
    l=[]
    l[:0]=s
    
    a.append(l)
 
count=0
sx=sy=0
ex=ey=0
for i in range(n):
    for j in range(m):
        if a[i][j]=='A':
            sx=i
            sy=j
        if a[i][j]=='B':
            ex=i
            ey=j
 
vis= {} # List to keep track of visited nodes.
queue = []
bfs(vis,a,[sx,sy])
