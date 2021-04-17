
def multiply(a,b):
    mul=[[0 for i in range(6)]for j in range(6)]
    for i in range(6):
        for j in range(6):
            mul[i][j]=sum(a[i][k]*b[k][j] for k in range(6))%mod
    return mul
def solve():
    n=int(input())
    if n<7:return 2**(n-1)
    F=[[1,1,1,1,1,1],
       [1,0,0,0,0,0],
       [0,1,0,0,0,0],
       [0,0,1,0,0,0],
       [0,0,0,1,0,0],
       [0,0,0,0,1,0]]
    M=F.copy()
    n-=6
    while n:
        if n%2:
            F=multiply(F,M)
        M=multiply(M,M)
        n//=2
    B=[16,8,4,2,1,1]
    return sum(F[0][i]*B[i] for i in range(6))%mod
mod=10**9+7
print(solve())

