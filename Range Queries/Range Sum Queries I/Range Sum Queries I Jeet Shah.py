from sys import stdin as stin, stdout as stout


def get_ints(): return map(int, stin.readline().split())
def get_list(): return list(map(int, stin.readline().split()))
def get_int(): return int(stin.readline())
def get_str(): return stin.readline()


n, p = get_ints()
x = get_list()
summation = [x[0]]
for i in range(1, n):
    summation.append(summation[i-1]+x[i])
for _ in range(p):
    a, b = get_ints()
    if a == 1:
        print(summation[b-1])
    else:
        print(summation[b-1] - summation[a-2])
