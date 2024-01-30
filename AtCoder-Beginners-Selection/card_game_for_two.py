N = int(input())
a_list = list(map(int, input().split()))

def pop_max_from_list(numbers):
    # リストが空でないことを確認
    if not numbers:
        return None  # リストが空の場合、Noneを返す

    # リストの最大値を見つける
    max_number = max(numbers)

    # 最大値をリストから削除
    numbers.remove(max_number)

    return max_number

alice = 0
bob = 0

for i in range(N):
    if i % 2 == 0:
        alice += pop_max_from_list(a_list)
    else:
        bob += pop_max_from_list(a_list)

print(alice - bob)