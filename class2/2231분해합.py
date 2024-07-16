def split_digits(n):
    # 입력받은 정수 n를 문자열로 바꾼 후, 다시 int타입으로 바꿔 리스트에 저장. 
    digit_list = [int(digit) for digit in str(n)]
    return digit_list

result_list = []
n = int(input())
for i in range(1, n):
    t = n - i
    temp = n - i # temp를 정의한 이유 -> t는 누적합을 구해야하는데, 누적합을 구하기 전의 원본이 필요해서
    for k in split_digits(t):
        t += k 
    if (n == t): 
        result_list.append(temp)

if result_list:
    result = min(result_list)
else:
    result = 0

print(result)







