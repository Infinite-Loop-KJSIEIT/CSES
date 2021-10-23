import sys
input=sys.stdin.readline
n,k=map(int,input().split())
a=[True]*n
i=0
ans=[]
while True:
    ic=0
    while ic<k:
        if a[i]:
            ic+=1
        i+=1
        i%=n
    while not a[i]:
        i+=1
        i%=n
    
    
    
    