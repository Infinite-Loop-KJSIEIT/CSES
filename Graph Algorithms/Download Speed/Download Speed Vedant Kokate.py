import sys
def get_ints(): return map(int, sys.stdin.readline().strip().split())
def Bfs(C, F, s, t):  
        n = len(C)
        queue = []
        queue.append(s)
        global level
        level = n * [0]  
        level[s] = 1  
        while queue:
            k = queue.pop(0)
            for i in range(n):
                    if (F[k][i] < C[k][i]) and (level[i] == 0): 
                            level[i] = level[k] + 1
                            queue.append(i)
        return level[t] > 0


def Dfs(C, F, k, cp):
        tmp = cp
        if k == len(C)-1:
            return cp
        for i in range(len(C)):
            if (level[i] == level[k] + 1) and (F[k][i] < C[k][i]):
                f = Dfs(C,F,i,min(tmp,C[k][i] - F[k][i]))
                F[k][i] = F[k][i] + f
                F[i][k] = F[i][k] - f
                tmp = tmp - f
        return cp - tmp


def MaxFlow(C,s,t):
        n = len(C)
        F = [n*[0] for i in range(n)] 
        flow = 0
        while(Bfs(C,F,s,t)):
               flow = flow + Dfs(C,F,s,10**20)
        return flow
n,m=get_ints()
C=[[0 for i in range(n)]for j in range(n)]
for i in range(m):
    a,b,c=get_ints()
    a,b=a-1,b-1
    C[a][b]+=c
source = 0  
sink = n-1   

max_flow_value = MaxFlow(C, source, sink)
print (max_flow_value)
