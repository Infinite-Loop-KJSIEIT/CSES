#include<bits/stdc++.h>
#define mod 1000000007
#define pb push_back
#define ff first
#define ss second
#define ii pair<int,int>
#define vi vector<int>
#define vii vector<ii>
#define lli long long int
#define INF 1000000000
#define endl '\n'
#define ar array
const double PI = 3.141592653589793238460;
const int mxN = 2e5;
typedef std::complex<double> Complex;
typedef std::valarray<Complex> CArray;
 
using namespace std;
 
int n,m;
int main(){
    cin >> n >> m;
    set<ar<int,2>> s;
    for(int i = 0; i < n ; i++){
        int a;
        cin >> a;
        s.insert({a,i});
    }
    for(int i = 0; i < m; i++){
        int t;
        cin >> t;
        auto it = s.lower_bound({t+1,0});
        if(it == s.begin())
            cout << -1 << endl;
        else {
            it--;
            cout << (*it)[0] << endl;
            s.erase(it);
        }
    }
}