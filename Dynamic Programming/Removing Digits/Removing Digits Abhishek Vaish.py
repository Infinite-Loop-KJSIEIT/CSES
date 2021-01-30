n = int(input())
count  = 0
while n != 0 :
	m = max([int(i) for i in str(n)])
	n -= m
	count+=1
print(count)
