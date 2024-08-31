#include <bits/stdc++.h>
using namespace std;

int main() {
  // 入力受け取り
  int n;
  cin >> n;
  vector<int> cards(n);
  for (int i = 0; i < n; i++) {
    cin >> cards[i];
  }

  // cardsをソート
  sort(cards.rbegin(), cards.rend());

  // AliceとBobの得点を計算
  int alice = 0;
  int bob = 0;
  for (int i = 0; i < n; i++) {
    if (i % 2 == 0) {
      alice += cards[i];
    } else {
      bob += cards[i];
    }
  }

  // 結果出力
  cout << alice - bob << endl;
}
