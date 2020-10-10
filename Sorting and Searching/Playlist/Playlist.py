from sys import stdin, stdout
import sys 
def get_ints(): return map(int, sys.stdin.readline().strip().split())
#n = stdin.readline()
 
 
n=int(input())
a=list(get_ints())
seen={}
res=0
i=0
for j in range(n):
    if a[j] in seen.keys():
        i=max(i,seen[a[j]]+1)
   # print(i,j)
    res=max(res,j-i+1)
    seen[a[j]]=j
print(res)
