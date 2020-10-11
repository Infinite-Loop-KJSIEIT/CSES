from collections import deque

n = int(input())
arr = sorted(list(map(int, input().split())),reverse = True)
one_list = []
arr_sum = sum(arr) // 2
for a in arr:
    if (a <= arr_sum - sum(one_list)):
        one_list.append(arr.pop(arr.index(a)))
    if (sum(one_list) == arr_sum):
        break
print(sum(arr) - sum(one_list))
