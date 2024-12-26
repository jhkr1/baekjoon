num = int(input())
str_num = str(num)
count = 1
result = []
sum_result = 0
sum_str = ''

while(1):
    if(num // 10):
        num = num // 10
        count += 1
    else:
        break


# print(str_num[-1] + str_num[0] +str_num[1] + str_num[2] + str_num[3])
# str_num = str_num[-1] + str_num[0] +str_num[1] + str_num[2] + str_num[3]
# print(str_num[-1] + str_num[0] +str_num[1] + str_num[2] + str_num[3])

for i in range(count):
    sum_str += str_num[-1]
    for j in range(count - 1):
        sum_str += str_num[j]
    result.append(sum_str)
    str_num = sum_str
    sum_str = ''


for i in range(count):
    sum_result += int(result[i])

print(sum_result)


# 개선된 코드
def sum_of_rotations(N):
    # N을 문자열로 변환하여 자리수 확인
    N_str = str(N)
    d = len(N_str)
    current = N
    total_sum = 0

    for _ in range(d):
        total_sum += current
        # 숫자를 회전
        rotated_str = N_str[-1] + N_str[:-1]
        current = int(rotated_str)
        N_str = rotated_str

    return total_sum

# 입력 처리
N = int(input())  # N 입력
print(sum_of_rotations(N))  # 결과 출력