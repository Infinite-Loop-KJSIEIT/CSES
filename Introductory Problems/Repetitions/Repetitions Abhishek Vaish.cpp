#include<iostream>
 
using namespace std;
 
int main()
{
	int prev_best = 0 , curr_best = 1 ;
	string dna;
	cin>>dna;
	for (int i = 1; dna[i] != '\0'; ++i)
	{
		if (dna[i] == dna[i-1])
			++curr_best;
		else 
		{
			if(prev_best < curr_best)
				prev_best = curr_best;
			curr_best = 1;
		}
	}
	if(prev_best > curr_best)
		cout<<prev_best<<endl;
	else
		cout<<curr_best<<endl;
	return 0;
}