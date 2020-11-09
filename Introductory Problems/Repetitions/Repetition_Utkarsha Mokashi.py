s = input()
Max = 0
a = s[:1]
c = 0
for i in s:
    if i == a:
        c = c + 1
    else:
        if Max < c:
            Max = c
        a = i
        c = 1
if Max < c:
    Max = c
print(Max)
