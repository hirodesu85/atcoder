from itertools import combinations

N, P, Q = map(int, input().split())
A = list(map(int, input().split()))

count = 0

for a,b,c,d,e in combinations(A, 5):
    if a%P*b%P*c%P*d%P*e%P == Q:
        count += 1

print(count)