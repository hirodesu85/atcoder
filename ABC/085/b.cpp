#include <bits/stdc++.h>
using namespace std;

int main() {
  int n;
  cin >> n;
  set<int> d;
  for (int i = 0; i < n; i++) {
    int di;
    cin >> di;
    d.insert(di);
  }
  cout << d.size() << endl;
}
