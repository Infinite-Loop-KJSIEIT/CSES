from fractions import Fraction as f
n,k=map(int,input().split())
ans=f(0,1)

for i in range(1,k+1):
    ans+=i*(f(i,k)**n-f(i-1,k)**n)

print(f"{ans.numerator/ans.denominator:.6f}")