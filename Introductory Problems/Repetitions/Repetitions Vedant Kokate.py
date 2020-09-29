import sys
from sys import stdin
def get_ints(): return map(int, sys.stdin.readline().strip().split())
 
s=stdin.readline()
 
l=1
m=-1
for i in range(len(s)-1):
    if s[i]==s[i+1]:
        l+=1
    else:
        if m<l:
            m=l
        l=1
print(max(l,m))
