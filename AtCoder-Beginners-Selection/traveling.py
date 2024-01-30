N = int(input())
plan = [list(map(int, input().split())) for _ in range(N)]

def can_travel(plan):
    # 初期位置と時刻を設定
    current_x, current_y, current_t = 0, 0, 0

    for t, x, y in plan:
        # 前の目的地からの距離
        distance = abs(x - current_x) + abs(y - current_y)
        # 経過時間
        time_diff = t - current_t

        # 経過時間が距離より短い、または経過時間と距離の差が奇数の場合は不可能
        if time_diff < distance or (time_diff - distance) % 2 != 0:
            return False

        # 現在の位置と時刻を更新
        current_x, current_y, current_t = x, y, t

    return True

if can_travel(plan):
    print('Yes')
else:
    print('No')
