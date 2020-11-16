n = int(input())
movies = [list(map(int,input().split())) for _ in range(n)]
movies.sort(key=lambda x : x[1])
ans,t = 0,0
for i in movies:
	if i[0] >= t:
		ans+=1
		t = i[1]
print(ans)