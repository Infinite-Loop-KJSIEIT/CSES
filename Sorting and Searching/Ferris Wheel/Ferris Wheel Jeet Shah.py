from sys import stdin as stin, stdout as stout


def get_ints(): return map(int, stin.readline().split())
def get_list(): return list(map(int, stin.readline().split()))
def get_int(): return int(stin.readline())
def get_str(): return stin.readline()


n, x = get_ints()
p = sorted(get_list())
i, j = 0, n-1
counter = 0
while i <= j:
    if i == j:
        counter += 1
        i += 1
    elif p[i] + p[j] <= x:
        counter += 1
        i += 1
        j -= 1
    else:
        counter += 1
        j -= 1
print(counter)
