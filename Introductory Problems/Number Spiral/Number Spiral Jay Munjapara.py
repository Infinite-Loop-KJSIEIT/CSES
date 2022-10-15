for tc in range(int(input())):
    y, x = list(map(int, input().split()))
    y, x = x, y
    if y < x:
        if x%2 == 0:
            ans = (((x)**2) - y + 1)
        else:
            ans = (((x-1)**2) + y)
    else:
        if y%2 == 1:
            ans = (((y)**2) - x + 1)
        else:
            ans = (((y-1)**2) + x)
    print(ans)