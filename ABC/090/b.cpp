#include <bits/stdc++.h>
using namespace std;

int main() {
  int a, b;
  cin >> a >> b;

  int count = 0;
  for (int i = a; i <= b; i++) {
    // 真ん中以外の桁を取り出す
    int first, second, fourth, fifth;
    first = i % 10;
    second = (i / 10) % 10;
    fourth = (i / 1000) % 10;
    fifth = (i / 10000) % 10;

    // 回文判定
    if (first == fifth && second == fourth) {
      count++;
    }
  }

  cout << count << endl;
}
