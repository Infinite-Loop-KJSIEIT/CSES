string = str(input())
all_occurance = list(set(string))
once = False
evens = []
evens_count = []
odd = []
odd_count = []
for a in all_occurance:
    counter = string.count(a)
    if counter % 2 == 0:
        evens.append(a)
        evens_count.append(counter//2)
    elif not once:
        once = True
        odd.append(a)
        odd_count.append(counter)
    else:
        print('NO SOLUTION')
ans = ""
for x, y in zip(evens, evens_count):
    ans = ans + (x * y)
for a, b in zip(odd, odd_count):
    ans = ans + (a * b)
for x, y in zip(evens[::-1], evens_count[::-1]):
    ans = ans + (x * y)

print(ans)
