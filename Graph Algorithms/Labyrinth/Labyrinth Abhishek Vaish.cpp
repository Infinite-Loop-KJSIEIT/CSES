#include <iostream>
#include<queue>
#include<stack>
using namespace std;
class Node{
	public :
		char c,fw;
		int px,py,visited ;
};
int main()
{
	int n,m;
	cin>>n>>m;
	Node a[n][m] ;
	char c;
	queue<pair<int,int>> q;
	for (int i = 0; i < n; ++i)
	{
		for (int j = 0; j < m; ++j)
		{
			Node n = Node();
			cin>>c;
			n.c = c;
			// n.x = i ; 
			// n.y = j ;
			n.visited = 0 ;
			n.fw = '\0';
			n.px = -1 ;
			n.py = -1 ;
			if(c == 'A')
			{
				q.push({i,j});
				n.visited = 1;
			}
			a[i][j] = n;
		}
	}

	/// BFS
	int dx[] = {0,0,-1,1};
	int dy[] = {1,-1,0,0};
	pair<int,int> u, v ;
	bool found = false;
	while(!found and !q.empty())
	{
		u = q.front() ;
		q.pop();
		for(int i = 0; i< 4; ++i )
		{
			v = {u.first+dx[i] , u.second + dy[i]};
			// cout<<v.first<<" "<<v.second<<endl;
			if (-1<v.first and v.first<n and -1<v.second and v.second<m)
			{
				if(a[v.first][v.second].c != '#' and a[v.first][v.second].visited != 1 )
				{
					a[v.first][v.second].visited = 1;
					a[v.first][v.second].px = u.first;
					a[v.first][v.second].py = u.second;

					if(dx[i]==0 and dy[i] == 1)
						a[v.first][v.second].fw = 'R';
					else if(dx[i]==0 and dy[i] == -1)
						a[v.first][v.second].fw = 'L';
					else if(dx[i]==1 and dy[i] == 0)
						a[v.first][v.second].fw = 'D';
					else if(dx[i]==-1 and dy[i] == 0)
						a[v.first][v.second].fw = 'U';

					q.push(v);
					if(a[v.first][v.second].c == 'B')
					{
						found = true;
						break;
					}
				}
			}
			
		}
	}
	if(found)
	{
		cout<<"YES"<<endl;
		stack<char> s;
		while(a[v.first][v.second].c != 'A' )
		{
			s.push(a[v.first][v.second].fw);
			v = {a[v.first][v.second].px, a[v.first][v.second].py};
		}
		cout<<s.size()<<endl;
		while(!s.empty())
		{
			cout<<s.top();
			s.pop();
		}
	}
	else
		cout<<"NO"<<endl;
	return 0;
}