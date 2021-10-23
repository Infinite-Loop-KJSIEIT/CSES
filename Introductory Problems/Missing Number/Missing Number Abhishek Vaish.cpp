#include<iostream>
 
using namespace std;
 
int main()
{
	int n,x;
	cin>>n;
	int a[n+1] = {0};
	for (int i = 1; i < n; ++i)
	{
		cin>>x;
		a[x] = 1;
	}
	for (int i = 1 ; i <= n; ++i)
	{
		if(a[i] != 1)
		{
			cout<<i;
			break;
		}
	}
 
	
	return 0;
}