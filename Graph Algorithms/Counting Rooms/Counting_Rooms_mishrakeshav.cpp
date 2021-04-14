#include<bits/stdc++.h>
#include <sys/resource.h>
#define INF 1000000000
#define endl '\n'
const double PI = 3.141592653589793238460;
const int mxN = 2e5;


using namespace std;
void dfs(vector<vector<char>>& grid, int n, int m, int i, int j){
    grid[i][j] = 'v';
    
    if((i-1) >= 0 &&  grid[i-1][j] =='.'){
        dfs(grid,n,m,i-1,j);
    }
    if((j-1) >= 0 && grid[i][j-1] == '.'){
        dfs(grid,n,m,i,j-1);
    }
    if((j + 1) < m && grid[i][j+1] == '.'){
        dfs(grid,n,m,i,j+1);
    }
    if((i+1) < n  && grid[i+1][j] == '.'){
        dfs(grid,n,m,i+1,j);
    }
    
    
} 
int main(){
    rlimit cpu_time{.rlim_cur = 1, .rlim_max = 5}; 
    setrlimit(RLIMIT_CPU, &cpu_time);
    ios_base::sync_with_stdio(0);
    vector<vector<char>> grid;
    int m,n;
    char s;
    cin >> n >> m;
    for(int i = 0; i < n; i++){
        vector<char> v;
        for(int j = 0; j < m; j++){
            cin >> s;
            v.push_back(s);
        }
        grid.push_back(v);
    }
    int count = 0;
    for(int i = 0; i < n; i++){
        for(int j = 0; j < n; j++){
            if(grid[i][j] == '.') {
                // for(int i = 0; i < n; i++){
                //     for(int j = 0; j < m; j++){
                //         cout << grid[i][j];
                //     }
                //     cout << endl;
                // }
                // cout << endl;
                dfs(grid,n,m,i,j);
                count++;
                
            }
        }
    }
    cout << count << endl;
}