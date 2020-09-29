import sys 
def get_ints(): return map(int, sys.stdin.readline().strip().split())
    
n=int(input())
print(pow(2,n,10**9+7))
    
        
