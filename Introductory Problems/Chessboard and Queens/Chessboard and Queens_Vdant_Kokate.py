import sys
from itertools import permutations
def get_ints(): return map(int, sys.stdin.readline().strip().split())
 
def solve(i):
    global count
    if i==8:
        #print('here')
        count+=1
        return
    for j in range(8):
        if a[i][j]=='*': continue
        
        ok=True
        for k in range(i):
            if queen[k]==j or queen[k]==j+i-k or queen[k]==j-i+k:
                ok=False
                break
        if not ok:
            continue
        queen.append(j)
        solve(i+1)
        queen.pop()
    
 
 
a=["" for i in range(8)]
queen=[]
for i in range(8):
    a[i]=sys.stdin.readline().strip()
#print(a)
count=0
solve(0)
print(count)
    
