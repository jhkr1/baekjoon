from itertools import combinations

# 입력 받기
n, m = map(int, input().split())
num = list(map(int, input().split()))

max_sum = 0

# 가능한 모든 3개의 숫자 조합에 대해 합을 계산
for comb in combinations(num, 3):
    comb_sum = sum(comb)
    if comb_sum <= m:
        max_sum = max(max_sum, comb_sum)

print(max_sum)