# Source
# https://codeforces.com/blog/entry/82103
for _ in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    ans=0
    for i in range(n):
        if i%2:
            ans^=a[i]
    if ans:
        print('first')
    else:
        print('second')