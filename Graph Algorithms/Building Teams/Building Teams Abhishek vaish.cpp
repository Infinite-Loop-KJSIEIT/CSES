#include<iostream>
#include<vector>
#include<queue>

using namespace std;

bool bfs(vector<int> adj[] , int visited[], int team[],int n)
{
	queue<int> q;
	int u;
	for(int i = 1 ; i<=n ;++i)
	{
		if( visited[i] != 1)
		{
			q.push(i);
			visited[i] = 1;
			while(!q.empty())
			{
				u = q.front();
				q.pop();
				for(auto v:adj[u])
				{
					if(visited[v] != 1)
					{
						q.push(v);
						visited[v] = 1;
						team[v] = team[u]%2 + 1; // 0=>1 1=>0
					}
					else if(team[u] == team[v])
						return false;
				}
			}
		}
	}
	return true;
}

int main()
{
	int n,m;
	cin>>n>>m;
	int visited[n+1],team[n+1];
	vector<int> adj[n+1];
	for (int i = 0; i <= n; ++i)
	{
		visited[i] = 0;
		team[i] = 1;
	}
	int x,y;
	for (int i = 0; i < m; ++i)
	{
		cin>>x>>y;
		adj[x].push_back(y);
		adj[y].push_back(x);
	}
	if(bfs(adj,visited,team,n))
	{
		for(int i=1;i<=n;i++)
			cout<<team[i]<<" ";
		cout<<endl;
	}
	else
		cout<<"IMPOSSIBLE"<<endl;
	return 0;
}