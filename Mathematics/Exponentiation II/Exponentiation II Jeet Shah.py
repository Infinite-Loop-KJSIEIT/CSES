from sys import stdin as stin, stdout as stout


def get_ints(): return map(int, stin.readline().split())
def get_int(): return int(stin.readline())


mod = 10**9 + 7
# Fermat's little theorem
# pow = Equivalent to base**exp with 2 arguments or base**exp % mod with 3 arguments
for _ in range(get_int()):
    a, b, c = get_ints()
    print(pow(a, pow(b, c, mod-1), mod))
