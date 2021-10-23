from sys import stdin as stin, stdout as stout
from bisect import bisect_right
def get_ints(): return map(int, stin.readline().split())
def get_list(): return list(map(int, stin.readline().split()))
def get_int(): return int(stin.readline())
def get_str(): return stin.readline()


n = get_int()
k = get_list()
towers = []
j = 0
for i in range(n):
    pos = bisect_right(towers, k[i])
    if pos >= j:
        towers.append(k[i])
        j += 1
    else:
        towers[pos] = k[i]
print(j)
