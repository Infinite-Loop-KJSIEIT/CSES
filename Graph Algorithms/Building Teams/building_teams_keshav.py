from collections import deque
class Vertex:
    def __init__(self,data):
        self.data = data 
        self.visited = False
        self.group = 1 
        self.connections = []

def bfs(graph,i,color):
    q = deque()
    q.append(i)
    while q:
        new = deque()
        for j in q:
            vertex = graph[j]
            if vertex.visited: continue
            vertex.visited = True 
            vertex.group = color
            for k in vertex.connections:
                new.appendleft(k)
        color ^=1 
        q = new

def solve():
    n, m = map(int,input().split())
    graph = dict()
    for i in range(1,n+1):
        graph[i] = Vertex(i)
    for _ in range(m):
        a,b = map(int,input().split())
        graph[a].connections.append(b)
        graph[b].connections.append(a)
    # color all the vertices levelwise using bfs
    for i in range(1,n+1):
        if graph[i].visited: continue
        bfs(graph,i,0)
    
    # check if there are adjacent edges with the same color for 
    # impossible condition 
    for i in range(1,n+1):
        for j in graph[i].connections:
            if graph[i].group == graph[j].group:
                print('IMPOSSIBLE') 
                return 
    
    for i in range(1,n+1):
        print(graph[i].group + 1, end = " ")
    print()
        
if __name__ == '__main__':
    solve() 
