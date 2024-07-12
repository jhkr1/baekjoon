# 자기 점수 중에 최댓값 -> M
# 모든 점수를 (점수 / M) * 100

n = int(input())
scores = list(map(int, input().split()))
max_score = max(scores)
sum = 0

for sco in scores:
    sum += (sco/max_score) * 100

result = sum / n
print(result)
