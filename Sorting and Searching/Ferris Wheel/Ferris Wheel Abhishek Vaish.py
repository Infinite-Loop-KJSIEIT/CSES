n,x = map(int, input().split())
weights = sorted(list(map(int, input().split())))
i,j,count = 0,n-1,0
while i < j :
	if weights[i] + weights[j] <= x:
		i+=1
		j-=1
	else:
		j-=1
	count += 1
if i == j:
	count += 1
print(count)
