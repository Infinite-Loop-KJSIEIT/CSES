for _ in range(int(input())):
    x, y = map(int, input().split())
    a = (((2 * x) - y) / 3)
    b = (((2 * y) - x) / 3)
    if (a >= 0 and a.is_integer() and b >= 0 and b.is_integer()):
        print("YES")
    else:
        print("NO")
