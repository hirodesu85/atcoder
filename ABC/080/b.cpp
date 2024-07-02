#include <bits/stdc++.h>
using namespace std;

int main() {
  int n;
  cin >> n;

  int sum = 0;
  int tmp = n;
  while (tmp > 0) {
    sum += tmp % 10;
    tmp /= 10;
  }

  cout << (n % sum == 0 ? "Yes" : "No") << endl;
}
