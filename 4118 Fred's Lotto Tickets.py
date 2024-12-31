lotto = set()

for i in range(1, 50):
    lotto.add(i)

while(True):
    
    n = int(input())
    
    if(n == 0):
        break

    user_num = set()

    for i in range(n):
        user_lotto = input()
        user_num.update(map(int, user_lotto.split()))

    if(lotto == user_num):
        print('Yes')
    else:
        print('No')

    

    
    





# 개선된 코드
 # 상수: 1부터 49까지의 숫자 집합
LOTTO_NUMBERS = set(range(1, 50))

# 결과를 저장할 리스트
results = []

while True:
    # 티켓 개수 입력받기
    n = int(input())
    if n == 0:
        break

    # 모든 티켓에서 등장한 숫자를 저장할 집합
    user_num = set()

    # 티켓 입력 처리
    for _ in range(n):
        ticket = map(int, input().split())
        user_num.update(ticket)

    # 결과 확인
    if LOTTO_NUMBERS == user_num:
        results.append("Yes")
    else:
        results.append("No")

# 최종 결과 출력
print("\n".join(results))