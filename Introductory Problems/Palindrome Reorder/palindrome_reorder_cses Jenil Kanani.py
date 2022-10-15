arr = list(input())
narr = [0]*26
for i in arr:
    narr[ord(i) - 65] += 1
odd = 0
pos = "A"
place = 0
for i in range(25):
    if narr[i] % 2 != 0:
        odd += 1
        pos = chr(i+65)
        place = i
    if odd > 1:
        break
if odd > 1:
    print("NO SOLUTION")
else:
    for i in range(26):
        print(chr(i + 65) * (narr[i] // 2),end="")
    print(pos * odd,end="")
    for i in range(25,-1,-1):
        print(chr(i + 65) * (narr[i] // 2),end="")