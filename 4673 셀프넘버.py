# # def is_self_number(n):
# #     result = 0
# #     if n < 10:
# #         a, b = divmod(n, 10)
# #         result = n + b
# #     elif 10 <= n < 100:
# #         a, b = divmod(n, 10)
# #         result = n + a + b
# #     elif 100 <= n < 1000:
# #         a, b = divmod(n, 100)
# #         c, d = divmod(b, 10)
# #         result = n + a + c + d
# #     elif 1000 <= n < 10000:
# #         a, b = divmod(n, 1000)
# #         c, d = divmod(b, 100)
# #         e, f = divmod(d, 10)
# #         result = n + a + c + e + f
# #     elif n == 10000:
# #         result = 0
# #
# #     return result
#
#
# not_self_numbers = [is_self_number(i) for i in range(1, 10001)]
# self_number = []
#
# for i in range(1, 10001):
#     if i not in not_self_numbers:
#         self_number.append(i)
#
# for i in range(len(self_number)):
#     print(self_number[i])


# 개선된 코드
def is_self_number(n):
    """생성자를 계산하는 함수"""
    return n + sum(int(digit) for digit in str(n))

# 생성자가 되는 숫자를 저장
not_self_numbers = {is_self_number(i) for i in range(1, 10001)}

# 1부터 10000까지의 숫자 중 셀프 넘버 찾기
self_numbers = [i for i in range(1, 10001) if i not in not_self_numbers]

# 결과 출력
for number in self_numbers:
    print(number)

