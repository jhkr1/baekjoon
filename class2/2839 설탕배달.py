# 입력
n = int(input())

# 봉지 개수 초기화
result = -1

# 5kg 봉지를 최대한 사용하면서 나머지를 3kg로 처리
for i in range(n // 5, -1, -1):  # 5kg 봉지 개수를 줄여가며 탐색
    remainder = n - (i * 5)
    if remainder % 3 == 0:  # 나머지가 3으로 나누어떨어지는 경우
        result = i + (remainder // 3)
        break

# 결과 출력
print(result)



