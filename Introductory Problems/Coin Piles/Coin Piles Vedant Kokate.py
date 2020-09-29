import sys 
def get_ints(): return map(int, sys.stdin.readline().strip().split())
    
t=int(input())
for _ in range(t):
    a,b=get_ints()
    if (a+b)%3==0 and min(a,b)*2>=max(a,b):
        print("YES")
    else:
        print("NO")
