from sys import stdin, stdout
import sys 
def get_ints(): return map(int, sys.stdin.readline().strip().split())
#n = stdin.readline()
 
 
n=int(input())
a=list(get_ints())
M=0
temp=0
for i in a:
    temp+=i
    if temp<0:
        temp=0
    if temp>M:
        M=temp
if M==0:
    print(max(a))
else:
    print(M)
    
