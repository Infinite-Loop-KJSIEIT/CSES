from sys import stdin, stdout
import sys 
def get_ints(): return map(int, sys.stdin.readline().strip().split())
#n = stdin.readline()
 
 
n=int(input())
a=list(get_ints())
a.sort()
med=a[len(a)//2]
ans=0
for i in a:
    ans+=abs(med-i)
print(ans)
    
 
