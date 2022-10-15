l = list(input())
count, i, c = 1, 1, 1
while i < len(l):
    if l[i-1]==l[i]:
        c += 1
        if c > count:
            count = c
    else:
        c = 1
    i+=1
print(count)