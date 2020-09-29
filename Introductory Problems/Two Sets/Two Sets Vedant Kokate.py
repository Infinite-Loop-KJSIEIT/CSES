import sys 
def get_ints(): return map(int, sys.stdin.readline().strip().split())
    
n=int(input())
a=[]
b=[]
x=n%4
if x==1 or x==2:
    print("NO")
elif x==0:
    for i in range(1,n+1):
        if i%4==0 or i%4==1:
            a.append(i)
        else:
            b.append(i)
else:
    a=[1,2]
    b=[3]
    for i in range(4,n+1):
        if i%4==0 or i%4==3:
            a.append(i)
        else:
            b.append(i)
print("YES")
print(len(a))
for i in a: print(i,end=" ")
print()
print(len(b))
for i in b: print(i,end=" ")
            
    
        
    
        
 
        
        
        
            
        
    
                        
