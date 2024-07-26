#include <bits/stdc++.h>
using namespace std;

int main() {
  int n;
  cin >> n;
  vector<string> blue(n);
  for (int i = 0; i < n; i++) {
    cin >> blue[i];
  }

  int m;
  cin >> m;
  vector<string> red(m);
  for (int i = 0; i < m; i++) {
    cin >> red[i];
  }

  int ans = 0;
  for (int i = 0; i < n; i++) {
    int cnt = 0;
    for (int j = 0; j < n; j++) {
      if (blue[i] == blue[j]) {
        cnt++;
      }
    }
    for (int j = 0; j < m; j++) {
      if (blue[i] == red[j]) {
        cnt--;
      }
    }
    ans = max(ans, cnt);
  }

  cout << ans << endl;
}
