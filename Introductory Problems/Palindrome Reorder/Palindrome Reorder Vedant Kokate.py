import sys 
def get_ints(): return map(int, sys.stdin.readline().strip().split())
    
s=sys.stdin.readline().strip()
a=[0]*26
for i in s:
    a[ord(i)-65]+=1
ans=""
mid=""
odd=0
for i in range(26):
    if a[i]%2==1:
        odd+=1
if odd>1:
    print("NO SOLUTION")
else:
    for i in range(26):
        if a[i]%2==1:
            mid=chr(i+65)*a[i]
            a[i]=0
        a[i]//=2
        ans+=chr(i+65)*a[i]
    print(ans+mid+ans[::-1])
