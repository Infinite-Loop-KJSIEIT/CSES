import sys
from itertools import permutations
def get_ints(): return map(int, sys.stdin.readline().strip().split())
    
n=int(input())
a=list(get_ints())
g1=0
g2=0
m=10**15
for i in range(2**n):
    g1=0
    g2=0
    for j in range(n):
        if 1<<j&i:
            g1+=a[j]
        else:
            g2+=a[j]
    temp=abs(g1-g2)
    if temp<m:
        m=temp
print(m)
                        
    
            
    
    
    
   
    
