import sys
# def fibo_r(n: int):
#     if (n == 1 or n == 2):
#         return 1
#     else:
#         return (fibo_r(n-1) + fibo_r(n-2))

def fibo_dp(n :int):
    cnt = 0
    if n <= 2:
        cnt += 1
        return n
    dp = [0] * (n+1)

    dp[1] = 1
    dp[2] = 1

    for i in range(3, n+1):
        cnt += 1
        dp[i] = dp[i-1] + dp[i-2]

    return dp[n], cnt

n = int(sys.stdin.readline())
print(fibo_dp(n)[0], fibo_dp(n)[1])
