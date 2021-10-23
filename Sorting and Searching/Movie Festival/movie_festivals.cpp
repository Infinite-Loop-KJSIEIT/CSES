#include <bits/stdc++.h>
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
const int mxN = 2e5;
typedef std::complex<double> Complex;
typedef std::valarray<Complex> CArray;
using namespace std;
void solve1(){
    set<ii> s;
    int n;
    cin >> n;
    for(int i = 0; i < n; i++){
        int a,b;
        cin >> a >> b;
        s.insert({a,1});
        s.insert({b,-1});
    }
    int c = 0;
    int mxcount = 0;
    for(const auto a:s){
        if(a.ss == 1){
            c++;
        }else if(a.ss == -1 && c !=0){
            c = 0;
            mxcount++;
        }
    }
    cout << mxcount << endl;
}
void solve2(){
    int n;
    cin >> n;
    ar<int, 2> s[n];
    for(int i = 0; i < n; i++){
        cin >> s[i][1] >> s[i][0];
    }
    sort(s , s+n);
    int ans = 0, l = 0;
    for(auto a:s){
        if(a[1] >=l){
            ans++;
            l = a[0];
        }
    }
    cout << ans << endl;
 
}
int main() {
    rlimit cpu_time{.rlim_cur = 1, .rlim_max = 5}; 
    setrlimit(RLIMIT_CPU, &cpu_time);
    ios_base::sync_with_stdio(0);
    cin.tie(0); cout.tie(0);
    // freopen("input.txt", "r", stdin);
    // freopen("output.txt", "w", stdout);
    
    solve2();
}