def logic(n):
    while n != 1:
        print(n, end=' ')
        if n % 2 == 0:
            n = int(n / 2)
        else:
            n = (n * 3) + 1
    print(n)


if __name__ == "__main__":
    logic(int(input()))
