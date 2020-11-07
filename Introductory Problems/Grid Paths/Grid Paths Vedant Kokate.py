import sys
input=sys.stdin.readline
s=input()

stack=[(0,0,0)]
ans=0
while stack:
    x,y,d=stack.pop()
    if x==6 and y==6 and d==47:
        ans+=1
    if s[d]=='?':
        if x>0:
            stack.append((x-1,y,d+1))
        if x<6:
            stack.append((x+1,y,d+1))
        if y>0:
            stack.append((x,y-1,d+1))
        if y<6:
            stack.append((x,y+1,d+1))
    elif s[d]=='R' and y<6:
        stack.append((x,y+1,d+1))
    elif s[d]=='L' and y>0:
        stack.append((x,y-1,d+1))
    elif s[d]=='D' and x<6:
        stack.append((x+1,y,d+1))
    elif s[d]=='U' and x>0:
        stack.append((x-1,y,d+1))
        
        
        
    
