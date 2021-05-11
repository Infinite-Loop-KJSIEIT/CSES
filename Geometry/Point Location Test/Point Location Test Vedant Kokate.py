for _ in range(int(input())):
    x1,y1,x2,y2,x,y=map(int,input().split())
    a=(x-x1)*(y1-y2)-(y-y1)*(x1-x2)
    print('LEFT' if a>0 else 'RIGHT' if a<0 else 'TOUCH')