#include <bits/stdc++.h>
using namespace std;

int main() {
  // 入力受取
  int n;
  cin >> n;
  vector<int> a(n);
  for (int i = 0; i < n; i++) {
    cin >> a.at(i);
  }

  // 平均値の計算
  int sum = 0;
  for (int i = 0; i < n; i++) {
    sum += a.at(i);
  }
  int average = sum / n;

  // 平均値との差を出力
  for (int i = 0; i < n; i++) {
    cout << abs(a.at(i) - average) << endl;
  }
}
