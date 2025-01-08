def Dial(call_num):
    if call_num in 'ABC':
        return 2
    elif call_num in 'DEF':
        return 3
    elif call_num in 'GHI':
        return 4
    elif call_num in 'JKL':
        return 5
    elif call_num in 'MNO':
        return 6
    elif call_num in 'PQRS':
        return 7
    elif call_num in 'TUV':
        return 8
    elif call_num in 'WXYZ':
        return 9


call_num = input()
result = 0
for i in range(len(call_num)):
    result += Dial(call_num[i])
result += len(call_num)
print(result)

# 더 간결한 코드
# def Dial(call_num):
#     # 다이얼 시간 매핑
#     dial_map = {
#         'A': 3, 'B': 3, 'C': 3,
#         'D': 4, 'E': 4, 'F': 4,
#         'G': 5, 'H': 5, 'I': 5,
#         'J': 6, 'K': 6, 'L': 6,
#         'M': 7, 'N': 7, 'O': 7,
#         'P': 8, 'Q': 8, 'R': 8, 'S': 8,
#         'T': 9, 'U': 9, 'V': 9,
#         'W': 10, 'X': 10, 'Y': 10, 'Z': 10
#     }
#     return sum(dial_map[char] for char in call_num)
#
# # 입력 및 결과 출력
# call_num = input()
# print(Dial(call_num))