from collections import defaultdict
import queue


def bfs(node):
    q.put(node)
    visited[node] = True
    while not q.empty():
        v = int(q.get())
        for u in graph[v]:
            if not visited[u]:
                visited[u] = True
                q.put(u)


n, m = map(int, input().split())
graph = defaultdict(list)
for _ in range(m):
    x, y = map(int, input().split())
    graph[x-1].append(y-1)
    graph[y - 1].append(x - 1)

visited = [False] * n
connections = []
q = queue.Queue()
bfs(0)

for v in range(n):
    if visited[v] == False:
        bfs(v)
        connections.append([0, v])
    else:
        pass

print(len(connections))
for c in connections:
    for d in c:
        print(d+1, end=" ")
    print()
