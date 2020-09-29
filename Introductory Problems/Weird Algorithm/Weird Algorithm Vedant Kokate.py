n=int(input())*2
while n!=1:    
    n=n>>1 if n%2==0 else n*3+1
    print(n,end=" ")
