N = int(input())
x = 5
c = 0
while(x <= N):
    c += N // x
    x *= 5
print(c)