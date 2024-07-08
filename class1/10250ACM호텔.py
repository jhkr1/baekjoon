# T = T 개의 테스트 데이터
# H = 행수
# W = 열수
# N = 몇 번째 손님인지

# print(72 % 30) # 층수(N % H)
# print(10 % 6) # 층수 

T = int(input())
rows = 0
result = []


for i in range(T):
    cols = 1
    H, W, N = map(int, input().split())
    while(N - H > 0):
        cols += 1
        N = N - H
    rows = N % H # 층수
    if(rows == 0):
        rows = H
    # 방번호가 일의 자리일때 0을 붙여줌
    if(cols // 10 == 0):
        result.append(str(rows) + '0' + str(cols))
    else:
        result.append(str(rows) + str(cols))

for i in result:
    print(i)


# 개선된 코드
# T = int(input())
# result = []

# for i in range(T):
#     H, W, N = map(int, input().split())
#     # 층수 계산
#     floor = (N - 1) % H + 1
#     # 호수 계산
#     room_number = (N - 1) // H + 1
#     # 방 번호 형식 맞추기
#     result.append(f"{floor}{room_number:02d}")

# # 결과 출력
# for res in result:
#     print(res)