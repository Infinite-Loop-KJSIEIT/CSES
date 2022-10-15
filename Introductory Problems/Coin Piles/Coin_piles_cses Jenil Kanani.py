for _ in range(int(input())):
    a, b = map(int, input().split())
    t = ((a + b) // 3)
    if ((a + b) % 3) == 0 and a >= t and b >= t:
        print("YES")
    else:
        print("NO")