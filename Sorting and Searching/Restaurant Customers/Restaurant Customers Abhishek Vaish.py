n = int(input())
arrival = []
left = []
for _ in range(n):
	x,y = map(int, input().split())
	arrival.append(x)
	left.append(y)
arrival.sort()
left.sort()
max_ = 0
current = 0
i,j = 0,0
while i < n and j < n:
	if arrival[i] < left[j] :
		current +=1
		i+=1
	else :
		j+=1
		current -= 1
	if current > max_:
		max_ = current
print(max_)