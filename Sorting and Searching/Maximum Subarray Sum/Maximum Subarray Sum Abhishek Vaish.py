n = int(input())
a = list(map(int,input().split()))
max_sum = a[0]
current_sum = a[0]
for i in range(1,n) :
	if current_sum + a[i] > a[i] :
		current_sum += a[i]
	else :
		current_sum = a[i]
	if max_sum < current_sum :
		max_sum = current_sum
print(max_sum)
