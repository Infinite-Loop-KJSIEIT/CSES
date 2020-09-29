import sys 
def get_ints(): return map(int, sys.stdin.readline().strip().split())
    
n=int(input())
i=5
zero=0
while n//i>0:
    zero+=n//i
    i*=5
print(zero)
    
    
