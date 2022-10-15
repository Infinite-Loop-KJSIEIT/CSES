from itertools import groupby
print(max([len(''.join(g)) for k, g in groupby(str(input()))]))
