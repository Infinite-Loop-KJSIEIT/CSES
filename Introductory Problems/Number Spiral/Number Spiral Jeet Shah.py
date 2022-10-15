for _ in range(int(input())):
    y, x = map(int, input().split())
    y, x = y-1, x-1
    counter = 0
    if x >= y:
        if x == 0:
            counter += 1
            pass
        elif x % 2 != 0:
            counter += 1
            counter += (x + 1) // 2
            n = x // 2
            counter += (8 * (n * (n + 1) // 2)) - n
            counter += y
        else:
            counter += 1
            counter += (x) // 2
            n = x // 2
            counter += (8 * (n * (n + 1) // 2)) - n
            counter -= y
    else:
        if y % 2 != 0:
            n = (y + 1)//2
            counter += n
            n = n - 1
            counter += ((8 * (n * (n + 1) // 2)) + 3 * n) + 3
            counter -= x
        else:
            n = (y)//2
            counter += n + 1
            n = n - 1
            counter += ((8 * (n * (n + 1) // 2)) + 3 * n) + 3
            counter += x
    print(counter)
