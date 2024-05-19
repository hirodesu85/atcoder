#include <bits/stdc++.h>
using namespace std;

int main() {
  int s;
  cin >> s;

  int ans = 0;
  ans += s % 10;
  ans += (s / 10) % 10;
  ans += (s / 100) % 10;

  cout << ans << endl;
}
