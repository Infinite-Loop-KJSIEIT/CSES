import sys
from itertools import permutations
def get_ints(): return map(int, sys.stdin.readline().strip().split())
    
s=sys.stdin.readline().strip()
per =list(permutations(s))
a=set()
for i in per:
    a.add(''.join(i))
ans=[]
 
for i in a:
    ans.append(i)
ans.sort()
print(len(a))
for i in ans:
    print(i)
    
        
    
        
 
        
