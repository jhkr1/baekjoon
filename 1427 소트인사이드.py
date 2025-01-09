n = int(input())  # 입력 받기
str_n = str(n)  # 숫자를 문자열로 변환
n_list = [int(digit) for digit in str_n]  # 각 자리수를 리스트로 변환
n_list.sort(reverse=True)  # 내림차순 정렬
result = ''.join(map(str, n_list))  # 정렬된 리스트를 문자열로 변환하고 합치기

print(result)  # 결과 출력

# 개선된 코드
# 숫자를 입력받음
n = input()

# 각 자리수를 내림차순으로 정렬
sorted_n = ''.join(sorted(n, reverse=True))

# 결과 출력
print(sorted_n)