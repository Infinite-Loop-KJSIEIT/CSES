#include <iostream>
#include<set>

using namespace std;

int main()
{
	int n,m,x;
	multiset<int> s ;
	cin>>n>>m;
	while(n--){
		cin>>x;
		s.insert(x); // logN ascending order
	}

	while(m--){
		cin>>x;
		auto it = s.upper_bound(x);
		if (it == s.begin())
			cout<<-1<<endl;
		else{
			it--;
			cout<<*it<<endl;
			s.erase(it);
		}
		
	}

	return 0;
}