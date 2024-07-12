# # 이 코드의 문제점 연속된 3가지 숫자만 뽑아서 합을 구함.
# # but 1번째 카드, 2번째 카드, 6번째 카드가 가장 큰 합이 될 수도 있다.
# n, m = map(int, input().split())
# num = list(map(int, input().split()))
# result = []


# for i in range(len(num) - 3):
#     sum = 0
#     for j in range(i, i+3):
#         sum += num[j]
#     if(sum <= m):
#         result.append(sum)


# max_result = max(result)

# print(max_result)

n, m = map(int, input().split())
num = list(map(int, input().split()))
result = []


for i in range(len(num) - 2):
    for j in range(i+1, len(num) - 1):
        for k in range(j+1, len(num)):
                sum = 0
                sum += num[i] + num[j] + num[k]
                if(sum <= m):
                     result.append(sum)

max_result = max(result)
print(max_result)
    

        


# 첫 번째 + 두 번째 + 세 번째
# 첫 번째 + 두 번째 + 네 번째
# 첫 번째 + 두 번째 + 다섯 번째
# 첫 번째 + 세 번째 + 네 번째
# 첫 번째 + 세 번째 + 다섯 번째
    



