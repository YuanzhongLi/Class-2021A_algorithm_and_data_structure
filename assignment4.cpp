#include <bits/stdc++.h>
using namespace std;

#define int long long
#define rep(i,s,n) for (int i = s; i < n; i++)
#define pb push_back
#define endl "\n"

class Dijkstra {
  int INF = 1001002003004005006ll;
  int WHITE = 0; // 未到達
  int GRAY = 1; // 到達
  int BLACK = 2; // 探索済み
public:
  int V; // 頂点数
  // <node, cost>
  vector<vector<pair<int, int>>> graph;
  vector<int> color;
  vector<int> dist;
  vector<int> parent;

  Dijkstra(int v): V(v) {
    graph.resize(v);
    color.resize(v);
    dist.resize(v);
    parent.resize(v);
  }

  void add_edge(int from, int to, int cost) {
    graph[from].pb(make_pair(to, cost));
  }

  void min_path(int s) {
    // <cost, node>
    priority_queue<pair<int, int>> PQ;

    // 初期化
    for (int i = 0; i < V; i++) {
      dist[i] = INF;
      color[i] = 0;
    }

    dist[s] = 0;
    PQ.push(make_pair(0ll, s));
    color[s] = GRAY;

    while (!PQ.empty()) {
      auto f = PQ.top(); PQ.pop();
      int u = f.second;
      if (color[u] == BLACK) continue;
      color[u] = BLACK;

      for (int j = 0; j < graph[u].size(); j++) {
        int v = graph[u][j].first;
        if (color[v] == BLACK) continue;
        if (dist[v] > dist[u] + graph[u][j].second) {
          dist[v] = dist[u] + graph[u][j].second;
          parent[v] = u; // 経路を求めるために親ノードを更新
          // priority_queueはデフォルトで大きい値を優先するため-1をかける
          PQ.push(make_pair(-dist[v], v));
          color[v] = GRAY;
        }
      }
    }
  }

  vector<int> min_route(int root, int e) {
    vector<int> ret;
    int p = e;
    while (p != root) {
      ret.pb(p);
      p = parent[p];
    }
    ret.pb(root);
    reverse(ret.begin(), ret.end());
    return ret;
  }
};

signed main() {
  ios::sync_with_stdio(false);
  cin.tie(0);

  int N = 10;
  Dijkstra dijkstra(N);
  rep(i,0,N) rep(j,0,N) {
    int c; cin >> c;
    dijkstra.add_edge(i, j, c);
  }

  dijkstra.min_path(0);

  cout << "最短経路長" << endl;
  rep(i,0,N) {
    cout << dijkstra.dist[i] << ((i+1 < N) ? " " : "\n");
  }

  cout << "始点0からの最短経路" << endl;
  rep(i,0,N) {
    vector<int> route = dijkstra.min_route(0, i);
    int M = route.size();
    cout << 0 << " -> " << i << ": ";
    rep(j,0,M) {
      cout << route[j] << ((j+1 < M) ? " " : "\n");
    }
  }
};
