#include<iostream>
using namespace std;
int main()
{
	int n;
	cin>>n;
	if (n == 1 )
		cout<<1<<endl;
	else if (n == 2 || n == 3)
		cout<<"NO SOLUTION"<<endl;
	else if(n==4)
		cout<<"2 4 1 3 "<<endl;
	else 
	{
		int a[n+1] ,x = 1;
		for (int i = 0; i < n; i+=2)
			a[i] = x++;
		for (int i = 1; i < n; i+=2)
			a[i] = x++;
		for(int i = 0 ; i < n ; ++i)
			cout<<a[i]<<" ";
		cout<<endl;
	}
	return 0;
}