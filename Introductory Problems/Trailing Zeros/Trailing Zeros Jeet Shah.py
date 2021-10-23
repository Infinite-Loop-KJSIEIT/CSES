n = int(input())
count = 0
i = 5
while (n/i >= 1):
    count += int(n/i)
    i *= 5
print(int(count))
