N, A, B = map(int, input().split())
total = 0

def is_sum_of_digits_in_range(n, a, b):
  # 各桁の数字の合計を計算
  sum_of_digits = sum(int(digit) for digit in str(n))

  # 合計が指定された範囲内にあるか判断
  return a <= sum_of_digits <= b

for i in range(1, N + 1):
  if is_sum_of_digits_in_range(i, A, B):
    total += i

print(total)