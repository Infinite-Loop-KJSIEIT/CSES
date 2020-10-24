from collections import deque
class Vertex:
    def __init__(self,data):
        self.data = data 
        self.color  = 0  
        self.parent = -1 
        self.connections = []


def dfs(graph, v):
    stack = []
    stack.append(v)
    while len(stack):
        
        v = stack.pop()
        graph[v].color = 1 
        for u in graph[v].connections:
            if u == graph[v].parent: continue
            if graph[u].color == 0:
                graph[u].parent = v 
                stack.append(u)
            elif graph[u].color == 1:
                return [u,v]
    graph[v].color = 2 
    return False 


def detect_cyle(graph,n):
    start , end = -1, -1
    for i in range(1,n+1):
        if graph[i].color == 0 :
            k = dfs(graph,i)
            if k:
                start,end = k 
                break
    if start == -1:
        print("IMPOSSIBLE")
    else:
        path = []
        path.append(start)
        while end!=start:
            path.append(end)
            end = graph[end].parent
        path.append(start)
        print(len(path))
        print(*path)


def solve():

    n, m = map(int, input().split())
    graph = {}
    for i in range(1,n+1):
        graph[i] = Vertex(i)
    
    for _ in range(m):
        a,b = map(int,input().split())
        graph[a].connections.append(b)
        graph[b].connections.append(a)
    
    detect_cyle(graph,n)

if __name__ == '__main__':
    solve()