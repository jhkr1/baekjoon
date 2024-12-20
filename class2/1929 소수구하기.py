# 소수 판별 함수
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

# 입력
m, n = map(int, input().split())

# 결과 출력
for i in range(m, n + 1):
    if is_prime(i):
        print(i)