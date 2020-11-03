for _ in range(int(input())):
    y,x = list(map(int,input().split()))
    if y <= x :   # 2 3
        if x % 2 != 0 :   # 3
            print(x**2 - y + 1)  
        else :
            print((x-1)**2 + y )
    elif y > x:
        if y % 2 != 0 :
            print((y-1)**2 + x ) 
        else :
            print(y**2 - x + 1) 