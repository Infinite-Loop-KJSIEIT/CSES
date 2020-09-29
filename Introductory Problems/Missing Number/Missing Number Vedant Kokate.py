import sys 
def get_ints(): return map(int, sys.stdin.readline().strip().split())
def inputs():sys.stdin.readline()
n=int(input())
a=list(get_ints())
ch=[0]*n
for i in a:
    ch[i-1]=1
#print(ch)
for i in range(n):
    if ch[i]==0:
        print(i+1)
        break
