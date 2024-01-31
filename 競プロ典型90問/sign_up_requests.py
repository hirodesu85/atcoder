N = int(input())
S_list = set()

for i in range(N):
  S = input()
  if S not in S_list:
    S_list.add(S)
    print(i+1)