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
    int parent;
    vector<int> connections;
};
void printPath(unordered_map<int, Vertex>& graph, int n){
    vector<int> path;
    int i = n;
    while ( i != -1){
        path.push_back(graph[i].data);
        i = graph[i].parent;
    }
    cout << path.size() << endl;
    for(int i = path.size()-1; i >=0; i--){
        cout << path[i] << " ";
    }
    cout << endl;
}
void bfs(unordered_map<int, Vertex>& graph, int n){
    queue<Vertex> s;
    s.push(graph[1]);
    while(!s.empty()){
        Vertex v = s.front();
        s.pop();
        for(auto i: v.connections){
            if(graph[i].visited) continue;
            graph[i].visited = 1;
            graph[i].parent = v.data;
            s.push(graph[i]);
        }
    }
}
int main(){
    rlimit cpu_time{.rlim_cur = 1, .rlim_max = 5}; 
    setrlimit(RLIMIT_CPU, &cpu_time);
    ios_base::sync_with_stdio(0);
    int n,m,a,b;
    cin >> n >> m;
    unordered_map<int , Vertex> graph;
    for(int i = 0; i < n; i++){
        graph[i+1] = Vertex();
        graph[i+1].data = i+1;
        graph[i+1].visited = 0;
    }
    
    for(int i = 0 ; i < m; i++){
        cin >> a >> b;
        graph[a].connections.push_back(b);
        graph[b].connections.push_back(a);
    }
    bfs(graph,n);
    graph[1].parent = -1;   
    if(graph[n].visited){
        // for(int i = 1; i<=n; i++){
        //     cout << graph[i].data << " " << graph[i].parent << endl;
        // }
        printPath(graph,n);
    }else{
        cout << "IMPOSSIBLE" << endl;
    }
}