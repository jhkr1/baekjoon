# a층의 b호에 살려면 자신의 아래(a-1층)의 1호부터 b호까지
# 사람들의 수의 합만큼 사람들을 데려와 살아야한다.
# 아파트는 0층부터, 각층은 1호부터 
# 0층의 i호는 i명이 산다.
# k층 n호에는 몇 명이 살고 있는지 출력하라.

# 무조건 이 구조는 재귀함수이다. 
# apartment[1][0] = apartment[0][0]
# apartment[1][1] = apartment[1][0] + apartment[0][1]
# apartment[1][2] = apartment[1][1] + apartment[0][2]
# apartment[1][3] = apratment[1][2] + apartment[0][3]
# apartment[1][4] = apartment[1][3] + apartment[0][4]
    
# def get_people(k, n):
#     # 0층일 경우, n호에는 n명이 산다.
#     if k == 0:
#         return n
#     # 각층의 1호에는 무조건 1명이 산다.
#     elif n == 1:
#         return 1
#     # 그 외의 경우, 재귀 호출
#     else:
#         return get_people(k,n-1) + get_people(k-1,n)



# T = int(input())
# result_list = []
# for i in range(T):
#     k = int(input())
#     n = int(input())
#     result_list.append(get_people(k, n))
# for i in result_list:
#     print(i)

# 재귀호출시 문제 발생 -> 시간 초과 -> 동적 프로그래밍(DP) 필요

def get_people(k, n):
    apartment = [[0] * (n+1) for _ in range(k+1)]

    # for i in apartment:
    #     print(i)

    for i in range(1, n+1):
        apartment[0][i] = i

    for i in range(1, k+1):
        for j in range(1, n+1):
            apartment[i][j] = apartment[i][j - 1] + apartment[i-1][j]

    return apartment[k][n]

T = int(input())
result_list = []
for _ in range(T):
    k = int(input())
    n = int(input())
    result_list.append(get_people(k, n))


for result in result_list:
    print(result)




