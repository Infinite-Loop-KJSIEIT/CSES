import sys
input=sys.stdin.readline
from heapq import heappop,heappush

n=int(input())
a=[]
for i in range(n):
    x,y=map(int,input().split())
    a.append((x,y,i))

a.sort(key=lambda x:x[0])
heap = [(-1, 1)]
 
ans, room_no = [0]*(n), 1

for s,e,i in a:
    last,rm=heappop(heap)
    if last<s:
        ans[i]=str(rm)
        heappush(heap, (e,rm))
    else:
        heappush(heap, (last,rm))
        room_no += 1
        ans[i]=str(room_no)
        heappush(heap, (e,room_no))

print(room_no)
print(" ".join(ans))


        