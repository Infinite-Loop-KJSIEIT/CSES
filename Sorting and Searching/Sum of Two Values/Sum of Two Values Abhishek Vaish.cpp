#include<iostream>
#include<vector>
#include<algorithm>
using namespace std;
 
int main()
{
	int n,x,a;
	cin>>n>>x;
	vector<pair<int,int>> v;
	for (int i=1 ;i<=n ;++i)
	{
	 	cin>>a;
	 	v.push_back({a,i});
	}
	sort(v.begin(), v.end());
	
	pair<int,int> p;
	bool found = false;
	for(int i=0;i<n;i++)
	{
		p = {x-v[i].first,0};
		auto it  = lower_bound(v.begin()+i+1,v.end(),p);
		if(it != v.end() && v[i].first == x-it->first)
		{
			cout<<v[i].second<<" "<<it->second<<endl;
			found = true;
			break;
		}
	}
	if (!found)
		cout<<"IMPOSSIBLE"<<endl;
	return 0;
}