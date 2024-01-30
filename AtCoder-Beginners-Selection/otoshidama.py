N, Y = map(int, input().split())

def is_valid_combination(n, y):
    # 10000円札の枚数を全探索
    for i in range(n + 1):
        # 5000円札の枚数を全探索
        for j in range(n - i + 1):
            # 1000円札の枚数を計算
            k = n - i - j

            # 合計金額を計算
            total = 10000 * i + 5000 * j + 1000 * k

            # 合計金額がy円であれば、組み合わせを出力
            if total == y:
                return i, j, k

    # 見つからなかった場合は、-1を返す
    return -1, -1, -1

x, y, z = is_valid_combination(N, Y)
print(x, y, z)

