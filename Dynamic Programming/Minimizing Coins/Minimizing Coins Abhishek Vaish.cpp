#include<iostream>
using namespace std;

int main()
{
	int MAXINT = 2147483646;
	int n,x,min;
	cin>>n>>x;
	int DP[x+1] = {MAXINT};
	DP[0] = 0;
	int coins[n];
	for (int i =0 ; i < n; ++i)
		cin>>coins[i];
	for (int i = 1 ; i <= x; ++i)
	{
		min = MAXINT;
		for (int c :coins)
		{
			if (i-c >= 0 && DP[i-c]+1 < min)
					min  = DP[i-c] + 1;
		}
		DP[i] = min;
	}
	if(DP[x] == MAXINT)
		cout<<-1;
	else
		cout<<DP[x];
}