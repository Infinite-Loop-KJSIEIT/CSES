import sys
input=sys.stdin.readline
def solve(n,k):
    # print('n =',n,'k =',k)
    if n==1:
        return 1
    if k<=(n+1)//2:
        # print('k<=(n+1)//2')
        if 2*k>n: 
            # print('2*k>n')
            return 2*k%n
        else: 
            # print('2*k<=n')
            return 2*k
    c=solve(n//2,k-(n+1)//2)
    # print('c =',c)
    if n%2: return 2*c+1
    else: return 2*c-1
# print('ans = ',solve(9,6))
for _ in range(int(input())):
    n,k=map(int,input().split())
    print(solve(n,k))
