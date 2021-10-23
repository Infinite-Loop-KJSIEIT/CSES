#include <iostream>
using namespace std;
int n,m,visited[1000][1000];
char a[1000][1000];

void DFS(int i,int j)
{
	if (i >= n || j>=m || i<0 ||j<0)
		return;
	if (a[i][j]=='.' && visited[i][j]==0)
	{
		//cout<<"Room["<<i<<"]["<<j<<"]"<<endl;
		visited[i][j] = 1;
		DFS(i+1,j);
		DFS(i,j+1);
		DFS(i-1,j);
		DFS(i,j-1);
	}
}

int main()
{
	int ans=0;
	cin>>n>>m;
	for(int i = 0; i<n;i++)
	{
		for(int j=0;j<m;j++)
		{
			cin>>a[i][j];
			visited[i][j] = 0;
		}
	}
	for(int i = 0; i<n;i++)
	{
		for(int j=0;j<m;j++)
		{
			if( a[i][j]=='.' && visited[i][j]==0)
			{
				DFS(i,j);
				++ans;
				//cout<<endl;
			}
		}
	}
	cout<<ans<<endl;
	return 0;
}