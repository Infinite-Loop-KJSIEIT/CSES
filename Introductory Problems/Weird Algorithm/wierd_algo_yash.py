x= int(input())
print(x,end=" ")
y=[]
while (x!= 1):
    if x%2==0:
        x/=2
        y.append(int(x))
    else:
        x= x*3 +1
        y.append(int(x))
print(*y)    