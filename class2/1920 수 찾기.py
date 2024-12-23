# N개의 정수 A[1], A[2], …, A[N]이 주어져 있을 때, 이 안에 X라는 정수가 존재하는지 알아내는 프로그램을 작성하시오.

# # 내가 짠 코드
# correct_num = int(input())
# correct_list = list(map(int, input().split()))

# num = int(input())
# list = list(map(int, input().split()))
# result_list = [0] * num

# for i in range(correct_num):
#     for j in range(correct_num):
#         if(list[i] == correct_list[j]):
#             result_list[i] = 1
#             break


# for i in range(num):
#     print(result_list[i])


# 개선된 코드
# correct_list의 원소들을 집합으로 변환
correct_num = int(input())
correct_list = set(map(int, input().split()))

# num은 비교할 수 있는 리스트
num = int(input())
check_list = list(map(int, input().split()))

# 결과 리스트
result_list = [0] * num

# 존재 여부를 set을 이용해 확인
for i in range(num):
    if check_list[i] in correct_list:
        result_list[i] = 1

# 결과 출력
for result in result_list:
    print(result)