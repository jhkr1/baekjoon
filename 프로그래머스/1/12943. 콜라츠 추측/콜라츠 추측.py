def solution(num):
    i = 0
    while num != 1 and i < 500:
        if num % 2 == 0:      # 짝수
            num //= 2
        else:                 # 홀수
            num = num * 3 + 1
        i += 1
    return i if num == 1 else -1