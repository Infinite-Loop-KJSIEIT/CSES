#include<iostream>
using namespace std;
 
int main()
{
	int m = 1000000007;
	int n,x,sum;
	cin>>n>>x;
	int DP[x+1] = {0};
	DP[0] = 1;
	int coins[n];
	for (int i =0 ; i < n; ++i)
		cin>>coins[i];
	for (int i = 1 ; i <= x; ++i)
	{
		sum = 0;
		for (int c :coins)
		{
			if (i-c >= 0 )
				sum  = (sum+DP[i-c])%m;
		}
		DP[i] = sum;
	}
 
	cout<<DP[x];
}
