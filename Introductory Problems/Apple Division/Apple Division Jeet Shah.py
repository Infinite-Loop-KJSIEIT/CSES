from sys import stdin as stin, stdout as stout

def get_list(): return list(map(int, stin.readline().split()))
def get_int(): return int(stin.readline())

n = get_int()
p = get_list()

temp = float('inf')
for i in range(2**n):
    a1, a2 = 0, 0
    for j in range(n):
        if 1 << j & i:
            a1 += p[j]
        else:
            a2 += p[j]
    temp = min(abs(a1-a2), temp)
print(temp)