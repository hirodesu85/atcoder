#include <bits/stdc++.h>
using namespace std;

int main() {
  // 入力受取
  int n; 
  cin >> n;
  vector<int> rules(n);
  for (int i = 0; i < n; i++) {
    cin >> rules[i];
  }

  // 処理
  int count = 0;
  vector<bool> visited(n, false);
  int current = 1;
  visited.at(0) = true;
  while (true) {
    current = rules.at(current - 1);
    count++;

    if (current == 2) {
      cout << count << endl;
      return 0;
    }
    if (visited.at(current - 1)) {
      cout << -1 << endl;
      return 0;
    }

    visited.at(current - 1) = true;
  }
}
