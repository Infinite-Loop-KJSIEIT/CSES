# Source
# https://codeforces.com/blog/entry/87585
n=int(input())
s=input()
# finding k


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
    stack=[]
    for i in s:
        if i=='(':
            stack.append('(')
        else:
            if len(stack)>0:
                stack.pop()
            else:
                return 0
    k=len(stack)
    n-=len(s)-k
    n=n//2-k
    if n<0:
        return 0
    ans=(k+1)*inv(n+k+1)*fact(2*n+k)*inv(fact(n))*inv(fact(n+k))
    ans%=mod
    return ans
print(solve(n))