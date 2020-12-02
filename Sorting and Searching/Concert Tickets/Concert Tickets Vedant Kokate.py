##Needs test run to understand this algo
##Ask me if in doubt
import sys
from bisect import bisect_right
input=sys.stdin.readline
def f():return map(int,input().split())
n,m=f()
h=list(f())
cnt=list(range(n+1))
h.sort()
#print(h)
ans=[]
for t in list(f()):
    old_pos = pos = bisect_right(h, t)
    while pos != cnt[pos]:
        pos = cnt[pos]
    while old_pos != pos:
        cnt[old_pos], old_pos = pos, cnt[old_pos]
    if pos:
        ans.append(h[pos - 1])
        cnt[pos] = pos - 1
    else:
        ans.append('-1')
for i in ans:print(i)