def fibo(n):
    if n==0:
        return(0,1)
    p=fibo(n>>1)
    c=p[0]*(2*p[1]-p[0]+mod)%mod 
    d=(p[0]**2+p[1]**2)%mod
    if n%2:
        return (d,(c+d)%mod)
    else:
        return (c,d)
n=int(input())
mod=10**9+7
print(fibo(n)[0])