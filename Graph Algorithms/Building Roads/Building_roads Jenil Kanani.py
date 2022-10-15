import collections

def bfs(start):
    if flag[start]:
        return
    que.append(start)
    flag[start] = 1
    while que:
        x = que.popleft()
        flag[x] = 1
        if arr[x]:
            for _ in arr[x]:
                if (not flag[_]):
                    que.append(_)
    toconnect.append(x)

n, m = map(int, input().split())
toconnect = []
flag = [0] * n
que = collections.deque()
arr = collections.defaultdict(list)
count = 0

for _ in range(m):
    x, y = map(int, input().split())
    arr[x - 1].append(y - 1)
    arr[y - 1].append(x - 1)
for i in range(n):
    if not flag[i]:
        count += 1
        bfs(i)
print(count - 1)
for k in range(len(toconnect) - 1):
    print(toconnect[k] + 1, toconnect[k + 1] + 1)