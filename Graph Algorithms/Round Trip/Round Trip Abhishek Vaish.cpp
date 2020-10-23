#include<iostream>
#include<vector>
#include<stack>
#include<queue>

using namespace std;

void track(int s, int d , pair<int,int> visited[], int parent[])
{
	stack<int> p1;  //path s in p1
	queue<int> p2;  //path d in p2
	// cout<<endl<<s<<" "<<d<<endl;
	// cout<<visited[s].second<<" "<<visited[d].second<<endl;
	int len = 0 ;
	if(visited[s].second > visited[d].second)
	{
		p1.push(s);
		s = parent[s];
		++len;
	}
	else if (visited[s].second < visited[d].second)
	{
		p2.push(d);
		d = parent[d];
		++len;
	}
	while(s != d)
	{
		p1.push(s);
		p2.push(d);
		s = parent[s];
		d = parent[d];
		len += 2;
	}
	p1.push(s);
	p2.push(d);
	len+=2;
	cout<<len<<endl;
	while(!p1.empty())
	{
		cout<<p1.top()<<" ";
		p1.pop();
	}
	while(!p2.empty())
	{
		cout<<p2.front()<<" ";
		p2.pop();
	}

}

pair<int,int> bfs(vector<int> adj[],pair<int,int> visited[],int parent[],int n)
{
	queue<int> q;
	int u;
	for (int i = 1; i <=n ; ++i)
	{
		if(visited[i].first == 0)
		{
			q.push(i);
			visited[i].first = 1;
			while(!q.empty())
			{
				u = q.front();
				q.pop();
				for(auto v : adj[u])
				{
					if(visited[v].first != 1)
					{
						q.push(v);
						visited[v].first = 1;
						visited[v].second = visited[u].second+1;
						parent[v] = u;
					}
					else if(parent[u] != v)
						return {u,v};
				}
			}
		}
	}
	return {0,0};
}


int main()
{
	int n,m ;
	cin>>n>>m;
	vector<int> adj[n+1];
	int parent[n+1];
	pair<int,int> visited[n+1];

	for (int i = 0; i <= n; ++i)
	{
		visited[i].first = 0;
		visited[i].second = 0;
		parent[i] = 0;
	}
	int x,y;
	for (int i = 0; i < m; ++i)
	{
		cin>>x>>y;
		adj[x].push_back(y);
		adj[y].push_back(x);
	}
	pair<int,int> p = bfs(adj,visited,parent,n);
	if(p.first != 0)
		track(p.first,p.second,visited,parent);
	else
		cout<<"IMPOSSIBLE"<<endl;
	return 0;
}