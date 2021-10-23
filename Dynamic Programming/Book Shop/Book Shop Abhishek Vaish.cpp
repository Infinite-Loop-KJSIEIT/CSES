#include<iostream>

using namespace std;

int main()
{
	int n,x;
	cin>>n>>x;

	int price[n];
	for (int &p:price)
		cin>>p;

	int pages[n];
	for(int &p:pages)
		cin>>p;

	// x columns, n rows

	int DP[n+1][x+1];
	for(int i = 0 ; i < x+1 ; i++)
		DP[0][i] = 0 ;
	for(int i = 0 ; i < n+1 ; i++)
		DP[i][0] = 0 ;


	for(int i = 1 ; i < n+1 ; i++)
	{
		for(int j = 1 ; j< x+1 ; j++)
		{
			DP[i][j] = DP[i-1][j];
			if(j-price[i-1] > -1 )
			{
				if (DP[i-1][j] < DP[i-1][j-price[i-1]] + pages[i-1] )
					DP[i][j] = DP[i-1][j-price[i-1]] + pages[i-1] ;				
			}

		}
	}

	cout<<DP[n][x];
	
	


	return 0 ;
}