# Source
# https://cp-algorithms.com/combinatorics/bracket_sequences.html
n=int(input())
mod=10**9+7
def inv(x):
    return pow(x,mod-2,mod)
def fact(x):
    f=1
    for i in range(2,x+1):
        f*=i
        f%=mod
    return f
def solve(n):
    if n%2==1:
        return 0
    n=n//2
    ans=inv(n+1)*fact(2*n)*inv(fact(n))*inv(fact(n))
    ans%=mod
    return ans
print(solve(n))