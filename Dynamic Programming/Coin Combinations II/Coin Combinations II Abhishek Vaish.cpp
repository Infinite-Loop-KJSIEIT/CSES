#include<iostream>
using namespace std;
 
int main()
{
	int m = 1000000007;
	int n,x;
	cin>>n>>x;
	int DP[n+1][x+1] ;
	for (int i = 0 ; i <= n ; ++i)
		DP[i][0] = 1;
	for (int i = 1; i <= x; ++i)
		DP[0][i] = 0 ;
 
	int coins[n];
	for (int i =0 ; i < n; ++i)
		cin>>coins[i];
 
	for (int i = 1 ; i <= n; ++i)
	{
		for(int j = 1 ; j <= x ;++j )
		{
			DP[i][j] = (DP[i-1][j])%m;
			if (j >= coins[i-1])
				DP[i][j] += (DP[i][j - coins[i-1]])%m ;
		}
	}
	cout<<DP[n][x]%m;
 
}