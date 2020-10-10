from sys import stdin, stdout
import sys 
def get_ints(): return map(int, sys.stdin.readline().strip().split())
#n = stdin.readline()
 
n=int(input())
a=[]
for i in range(n):
    a.append(list(get_ints()))
 
a.sort(key=lambda x: x[1])
#print(a)
end=a[0][1]
c=1
for i in range(1,n):
    if a[i][0]>=end:
        end=a[i][1]
        c+
