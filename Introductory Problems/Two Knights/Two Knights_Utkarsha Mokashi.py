n = int(input())
for i in range(1,n+1):
    a = (((i*i)*((i*i)-1))/2) - (4*(i-1)*(i-2))
    print(int(a))
