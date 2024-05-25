#include <bits/stdc++.h>
using namespace std;

int main() {
  int n;
  cin >> n;

  int ones_place = n % 10;
  int tens_place = (n / 10) % 10;
  int hundreds_place = (n / 100) % 10;
  int thousands_place = (n / 1000) % 10;

  if ((ones_place == tens_place && tens_place == hundreds_place) || (tens_place == hundreds_place && hundreds_place == thousands_place)) {
    cout << "Yes" << endl;
  } else {
    cout << "No" << endl;
  }
}
