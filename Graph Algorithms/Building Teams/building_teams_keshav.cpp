#include<bits/stdc++.h>
#include <sys/resource.h>
#define INF 1000000000
#define endl '\n'
const double PI = 3.141592653589793238460;
const int mxN = 2e5;
using namespace std;

class Vertex{
    public:
    int data;
    int visited;
    int group;
    vector<int> connections;
};

void bfs(unordered_map<int, Vertex>& graph, int i, int color){
    vector<int> q;
    q.push_back(i);
    while(q.size() != 0){
        vector<int> new_q;
        for(int j : q){
            if(graph[j].visited) continue;
            graph[j].visited = 1;
            for(int k: graph[j].connections){
                new_q.push_back(k);
            }
            graph[j].group = color;
        }
        color ^= 1;
        q = new_q;
    }
}
int main(){
    rlimit cpu_time{.rlim_cur = 1, .rlim_max = 5}; 
    setrlimit(RLIMIT_CPU, &cpu_time);
    ios_base::sync_with_stdio(0);
    int n, m,a,b;
    cin >> n >> m;
    unordered_map<int , Vertex> graph;
    for(int i = 0; i < n; i++){
        graph[i+1] = Vertex();
        graph[i+1].data = i+1;
        graph[i+1].visited = 0;
        graph[i+1].group = 0;
    }
    for(int i = 0 ; i < m; i++){
        cin >> a >> b;
        graph[a].connections.push_back(b);
        graph[b].connections.push_back(a);
    }
    for(int i = 1; i <=n ; i++){
        if(graph[i].visited) continue;
        bfs(graph,i,0);
    }
    for(int i = 1; i <= n; i++){
        for(int j:graph[i].connections){
            if(graph[i].group == graph[j].group){
                cout << "IMPOSSIBLE" << endl;
                return 0;
            }
        }
    }
    for(int i = 1; i <=n; i++){
        cout << graph[i].group + 1 << " ";
    }
    cout << endl;
}