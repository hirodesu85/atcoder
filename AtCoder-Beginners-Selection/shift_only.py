n = int(input())
a = input()
a_list = list(map(int, a.split()))
count = 0

def are_all_even(numbers):
    # リスト内の各数値に対してループ
    for num in numbers:
        # 奇数が見つかった場合、Falseを返す
        if num % 2 != 0:
            return False
    # ループを完了し、すべて偶数だった場合、Trueを返す
    return True

while are_all_even(a_list):
    a_list = [a / 2 for a in a_list]
    count += 1

print(count)

