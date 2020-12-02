r=range
f=lambda:list(map(int,input().split()))
x=f()
p=f()
l=[0]+sorted(p)+x
print(l,'l')
h=x[1]+2
print('h',h)
d={l[i]:[l[i-1],l[i+1]] for i in r(h)}
print(d)
m=max(l[i+1]-l[i] for i in r(h))
print('m',m)
k=[]
for i in p[::-1]:
    print(d)
    k+=m,
    a,b=d.pop(i)
    print(a,b,'a b')
    m=max(b-a,m)
    d[a][1]=b
    d[b][0]=a
print(*k[::-1])