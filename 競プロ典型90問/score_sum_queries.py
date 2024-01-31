N = int(input())
students = [list(map(int, input().split())) for i in range(N)]
Q = int(input())
questions = [list(map(int, input().split())) for i in range(Q)]

# 累積和を計算
cum_sum_1 = [0]
cum_sum_2 = [0]

for i in range(N):
  if students[i][0] == 1:
    cum_sum_1.append(cum_sum_1[-1]+students[i][1])
    cum_sum_2.append(cum_sum_2[-1])
  else:
    cum_sum_1.append(cum_sum_1[-1])
    cum_sum_2.append(cum_sum_2[-1]+students[i][1])

for i in range(Q):
  L = questions[i][0]
  R = questions[i][1]
  print(cum_sum_1[R]-cum_sum_1[L-1], cum_sum_2[R]-cum_sum_2[L-1])