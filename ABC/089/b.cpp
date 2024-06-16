#include <bits/stdc++.h>
using namespace std;

int main() {
  int n;
  string s;
  cin >> n;

  bool yellow = false;
  for (int i = 0; i < n; i++) {
    cin >> s;
    if (s == "Y") {
      yellow = true;
      break;
    }
  }

  if (yellow) {
    cout << "Four" << endl;
  } else {
    cout << "Three" << endl;
  }
}
