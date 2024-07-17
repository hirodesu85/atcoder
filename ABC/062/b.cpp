#include <bits/stdc++.h>
using namespace std;

int main() {
  int h, w;
  cin >> h >> w;

  vector<string> vec(h+2);
  for (int i = 0; i < h+2; i++) {
    if (i == 0 || i == h+1) {
      vec.at(i) = string(w+2, '#');
    } else {
      string s;
      cin >> s;
      vec.at(i) = "#" + s + "#";
    }
  }

  for (int i = 0; i < h+2; i++) {
    cout << vec.at(i) << endl;
  }
}
