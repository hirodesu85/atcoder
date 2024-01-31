H, W = map(int, input().split())
A = [ list(map(int,input().split(" "))) for i in range(H)]

def row_sums(array):
    # 各行の合計を格納するリストを初期化
    sums = []
    
    # 各行に対して合計を計算し、リストに追加
    for row in array:
        sums.append(sum(row))
    
    return sums

def column_sums(array):
    # 各列の合計を格納するリストを初期化
    sums = []
    
    # 各列に対して合計を計算し、リストに追加
    for i in range(len(array[0])):
        total = 0
        for row in array:
            total += row[i]
        sums.append(total)
    
    return sums

H_sum = row_sums(A)
W_sum = column_sums(A)

B = [[0 for i in range(W)] for j in range(H)]

for i in range(H):
    for j in range(W):
        B[i][j] = H_sum[i] + W_sum[j] - A[i][j]

for i in range(H):
    print(*B[i])