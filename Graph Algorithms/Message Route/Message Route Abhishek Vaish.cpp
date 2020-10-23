#include <iostream>
#include<vector>
#include<queue>
using namespace std;

int len =  1;
void traverse(int parent[],int i)
{
	if(parent[i] != 0)
	{
		++len;
		traverse(parent,parent[i]);
		cout<<parent[i]<<" ";
	}
	else
		cout<<len<<endl;
}

bool bfs(vector<vector<int>>& adj  ,int visited[] ,int parent[] ,int n)
{
	queue<int> q;
	q.push(1);
	visited[1] = 1;
	
	int u;
	while(!q.empty())
	{
		u = q.front();
		q.pop();
		for (auto v : adj[u])
		{
			if (visited[v] != 1)
			{
				visited[v] = 1;
				q.push(v);
				parent[v] = u;
				if (v == n)
					return true;
			}
		}
	}
	return false;
}


int main()
{
	int n,m,x,y;
	cin>>n>>m;
	int visited[n],parent[n];
	vector<vector<int>> adj;
	for(int i = 0 ;i <= n; ++i)
	{
		adj.push_back({});
		visited[i] = 0;
		parent[i] = 0;
	}
	for (int i = 0; i < m; ++i)
	{
		cin>>x>>y;
		adj[x].push_back(y);
		adj[y].push_back(x);
	}

	if (bfs(adj,visited,parent,n))
	{
		traverse(parent,n);
		cout<<n;
	}
	else
		cout<<"IMPOSSIBLE"<<endl;
	return 0;
}