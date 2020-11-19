#include<iostream>
using namespace std;
int main()
{
	long long int n,x=0;
	cin>>n;
	long long int a[n];
	cin>>a[0];
	for (int i = 1; i < n; ++i)
	{
		cin>>a[i];
		if(a[i] < a[i-1])
		{
			x+= (a[i-1] - a[i]);
			a[i] += (a[i-1] - a[i]);
		}
	}
	cout<<x<<endl;
	return 0;
}