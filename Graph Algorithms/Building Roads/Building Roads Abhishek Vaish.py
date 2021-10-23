from collections import deque 
def bfs():
	while(len(queue)):
		u = queue.popleft()
		for v in adj[u]:
			if not visited[v]:
				visited[v] = 1
				queue.append(v)
				
n,m = map(int, input().split())
adj = {i:[] for i in range(1,n+1)}
visited = [0]*(n+1)
visited[1] = 1
for i in range(m):
	x,y = map(int,input().split())
	adj[x].append(y)
	adj[y].append(x)
 
queue = deque()
queue.append(1)
bfs()
ans = []
n_road = 0
for i in range(1,n+1):
	if not visited[i]:
		visited[i] = 1
		n_road += 1
		ans.append([i-1,i])
		queue.append(i)
		bfs()
print(n_road)
for i in ans:print(i[0],i[1])