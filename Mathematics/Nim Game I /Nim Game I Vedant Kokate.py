for _ in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    ans=0
    for i in a:
        ans^=i
    if ans:
        print('first')
    else:
        print('second')