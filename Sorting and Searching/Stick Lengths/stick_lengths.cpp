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
int arr[mxN];
void solve() {
    int n;
    cin >> n;
    for(int i=0; i < n; i++){
        cin >> arr[i];
    }
    sort(arr,arr+n);
    int mid = arr[n/2];
    lli cost = 0;
    for(int i = 0; i < n; i++){
        cost += abs(arr[i]-mid);
    }
    cout << cost << endl;
}
 
int main() {
    rlimit cpu_time{.rlim_cur = 1, .rlim_max = 5}; 
    setrlimit(RLIMIT_CPU, &cpu_time);
    ios_base::sync_with_stdio(0);
    cin.tie(0); cout.tie(0);
    // freopen("input.txt", "r", stdin);
    // freopen("output.txt", "w", stdout);
    
    solve();
}