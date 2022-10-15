counter = 0
n = int(input())
while n:
    arr = (list(map(int, str(n))))
    n -= max(arr)
    counter += 1
print(counter)
