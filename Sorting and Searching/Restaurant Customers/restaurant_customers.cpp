#include<bits/stdc++.h>
#include <sys/resource.h>
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
typedef std::complex<double> Complex;
typedef std::valarray<Complex> CArray;
 
using namespace std;
 
int main(){
    rlimit cpu_time{.rlim_cur = 1, .rlim_max = 5}; 
    setrlimit(RLIMIT_CPU, &cpu_time);
    set<ar<int,2>> s;
    int n;
    cin >> n;
    for(int i =0 ; i < n; i++){
        int a , b;
        cin >> a >> b;
        s.insert({a,1});
        s.insert({b,-1});
    }
    int mx = 0, m = 0;
    for(const auto arr:s){
        m += arr[1];
        mx = max(m,mx);
    }
    cout << mx << endl;
 
}
