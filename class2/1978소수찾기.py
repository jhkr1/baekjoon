# N = int(input())
# num_list = input().split()
# result = 0

# for i in range(N):
#     num_list[i] = int(num_list[i])

# # 소수 = 1과 자기 자신으로만 나눠지는 숫자2 이상의 수
# # 즉, 2 ~ N-1까지 나눴을 때 나머지가 0이 되면 소수가 아님


# for i in range(N):
#     num = 2
#     while(True):
#         if(num_list[i] == 1):
#             break
#         if(num == num_list[i]):
#             result += 1
#             break
#         if(num_list[i] % num != 0):
#             num += 1
#         elif(num_list[i] % num == 0):
#             break
# print(result)
        
    
    
## 좀 더 간결한 코드
def is_prime(n):
    if (n <= 1):
        return False
    num = 2
    while num < n:
        if (n % num == 0):
            return False
        num += 1
    return True

N = int(input())
num_list = list(map(int, input().split()))
result = 0

for num in num_list:
    if is_prime(num):
        result += 1
print(result)