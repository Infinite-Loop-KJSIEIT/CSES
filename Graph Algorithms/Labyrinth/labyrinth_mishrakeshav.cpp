#include<bits/stdc++.h>
#include <sys/resource.h>
#define INF 1000000000
#define endl '\n'
const double PI = 3.141592653589793238460;
const int mxN = 2e5;
using namespace std;
class Vertex{
    public:
        char data;
        char parent;
        pair<int,int> position;
};

void printPath(vector<vector<Vertex>>& grid, int i, int j){
    stack<char> q;
    int count = 0;
    while (grid[i][j].parent != 'S'){  
        q.push(grid[i][j].parent);
        count++;
        if(grid[i][j].parent == 'L'){
            j++;
        }
        else if (grid[i][j].parent == 'R'){
            j--;
        }
        else if(grid[i][j].parent == 'U'){
            i++;
        }
        else{
            i--;
        }
    }
    cout << count << endl;
    while (!q.empty()){
        cout << q.top();
        q.pop();

    }
    cout << endl;
}

pair<int,int> bfs(vector<vector<Vertex>>& grid, int i, int j, int n, int m){

    queue<Vertex> q;
    q.push(grid[i][j]);
    while(!q.empty()){
        
        Vertex v = q.front();
        q.pop();
        int x,y;
        x = v.position.second;
        y = v.position.first;
        if(v.data == 'B'){
            return {x,y};
        }
        if(x + 1 < m && grid[y][x + 1].data != '#' && grid[y][x + 1].parent == 'N'){
            grid[y][x + 1].parent = 'R';
            q.push(grid[y][x + 1]);
        }
        if(x - 1 >= 0 && grid[y][x - 1].data != '#' && grid[y][x - 1].parent == 'N'){
            grid[y][x - 1].parent = 'L';
            q.push(grid[y][x - 1]);
        }
        if(y + 1 < n && grid[y + 1][x].data != '#' && grid[y + 1][x].parent == 'N'){
            grid[y + 1][x].parent = 'D';
            q.push(grid[y + 1][x]);
        }
        if(y - 1 >= 0 && grid[y - 1][x].data != '#' && grid[y-1][x].parent == 'N'){
            grid[y-1][x].parent = 'U';
            q.push(grid[y-1][x]);
        }
    }
    return {-1,-1};
}
int main(){
    rlimit cpu_time{.rlim_cur = 1, .rlim_max = 5}; 
    setrlimit(RLIMIT_CPU, &cpu_time);
    ios_base::sync_with_stdio(0);
    int n,m;
    char c;
    vector<vector<Vertex>> grid;
    cin >> n >> m;
    for(int i = 0; i < n; i++){
        vector<Vertex> v;
        for(int j = 0; j < m; j++){
            cin >> c;
            Vertex vertex = Vertex();
            vertex.data = c;
            vertex.position = {i,j};
            vertex.parent = 'N';
            v.push_back(vertex);
        }
        grid.push_back(v);
    }
    pair<int,int> ans = {-1,-1};
    for(int i = 0; i < n; i++){
        for(int j = 0; j < m; j++){
            if(grid[i][j].data == 'A'){
                grid[i][j].parent = 'S';
                ans = bfs(grid,i,j,n,m);
                break;
            }
        }
    }
    if(ans.first == -1){
        cout << "NO" << endl;
    }else{
        cout << "YES" << endl;
        printPath(grid,ans.second,ans.first);

    }
}