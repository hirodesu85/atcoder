def count_combinations(A, B, C, X):
    count = 0
    # 500円玉に関するループ
    for a in range(A + 1):
        # 100円玉に関するループ
        for b in range(B + 1):
            # 50円玉に関するループ
            for c in range(C + 1):
                # 合計金額の計算
                total = 500 * a + 100 * b + 50 * c
                # 合計金額がX円になる場合、カウントを1増やす
                if total == X:
                    count += 1
    return count

# 使用例
A = int(input()) # 500円玉の枚数
B = int(input()) # 100円玉の枚数
C = int(input()) # 50円玉の枚数
X = int(input()) # 目標金額
result = count_combinations(A, B, C, X)
print(result)
