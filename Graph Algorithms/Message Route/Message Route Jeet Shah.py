from collections import defaultdict
import queue

n, m = map(int, input().split())
vertices = [i + 1 for i in range(n)]
graph = defaultdict(list)
for _ in range(m):
    v, k = map(int, input().split())
    graph[v].append(k)
    graph[k].append(v)

q = queue.Queue()
q.put(1)

visited = [False] * (n+1)
visited[1] = True

prev = [0] * (n+1)
while q.empty() == False:
    node = q.get()
    neighnours = graph[node]

    for ne in neighnours:
        if visited[ne] == False:
            q.put(ne)
            visited[ne] = True
            prev[ne] = node

path = []
temp = int(n)
path.append(temp)
while temp != 1:
    if temp == 0:
        break
    temp = prev[temp]
    path.append(temp)

path.reverse()
if path[0] == 1:
    print(len(path))
    for p in path:
        print(p, end=" ")
else:
    print("IMPOSSIBLE")
