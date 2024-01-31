import math

A, B, C = map(int, input().split())

def gcd_of_three_numbers(a, b, c):
    # 最初の2つの数のGCDを計算
    gcd_first_two = math.gcd(a, b)
    # 上で得たGCDと3つ目の数のGCDを計算
    gcd_all_three = math.gcd(gcd_first_two, c)
    
    return gcd_all_three

gcd = gcd_of_three_numbers(A, B, C)
print(A//gcd + B//gcd + C//gcd - 3)