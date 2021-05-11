import sys
input=sys.stdin.readline
sys.setrecursionlimit(10**6)
def dfs(v):
    global cycle_end,cycle_start
    color[v]=1
    for u in g[v]:
        if color[u]==0:
            parent[u]=v
            if dfs(u):
                return True
        elif color[u]==1:
            cycle_end=v
            cycle_start=u
            return True
    color[v]=2
    return False


n,m=map(int,input().split())
g=[[]for i in range(n)]
for i in range(m):
    a,b=map(int,input().split())
    g[a-1].append(b-1)

color=[0]*n
parent=[-1]*n
cycle_end,cycle_start=-1,-1

for v in range(n):
    if color[v]==0 and dfs(v):
        break

if cycle_start==-1:
    print("IMPOSSIBLE")
else:
    # print(cycle_start,cycle_end)
    # print(parent)
    cycle=[cycle_start+1]
    v=cycle_end
    while v!=cycle_start:
        cycle.append(v+1)
        v=parent[v]
    cycle.insert(0,cycle[-1])
    print(len(cycle))
    print(*reversed(cycle))
