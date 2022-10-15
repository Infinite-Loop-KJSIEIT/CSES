from sys import stdin as stin, stdout as stout


def get_ints(): return map(int, stin.readline().split())
def get_int(): return int(stin.readline())


# pow = Equivalent to base**exp with 2 arguments or base**exp % mod with 3 arguments
mod = 10**9 + 7

for _ in range(get_int()):
    a, b = get_ints()
    print(pow(a, b, mod))
