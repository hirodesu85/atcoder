#include <bits/stdc++.h>
using namespace std;

int main() {
  int n;
  cin >> n;

  int min_div_count = 1000000000;
  for (int i = 0; i < n; i++) {
    int a;
    cin >> a;
    
    int div_count = 0;
    while (a % 2 == 0) {
      a /= 2;
      div_count++;
    }
    min_div_count = min(min_div_count, div_count);
  }

  cout << min_div_count << endl;
}
