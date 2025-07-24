import sys

n = int(sys.stdin.readline())
s = [0] * 301
for i in range(n):
    s[i] = int(sys.stdin.readline())

# dp 테이블 초기화
dp = [0] * 301

# 계단이 1개 또는 2개일 경우 예외 처리
if n == 1:
    print(s[0])
    exit()
if n == 2:
    print(s[0] + s[1])
    exit()

# DP 초기값 설정 (Base Case)
dp[0] = s[0]
dp[1] = s[0] + s[1]
dp[2] = max(s[0] + s[2], s[1] + s[2]) # 1번 -> 3번 or 2번 -> 3번

for i in range(3, n):
    # i-2에서 온 경우 vs i-3 -> i-1 -> i로 온 경우
    dp[i] = max(dp[i-2] + s[i], dp[i-3] + s[i-1] + s[i])

print(dp[n-1])
