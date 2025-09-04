def solution(n):
    new_num = ''
    answer = 0
    while n > 0:
        new_num += str(n % 3)
        n = n // 3

    new_num = new_num[-1::-1]

    for i in range(len(new_num)):
        answer += (3**i) * int(new_num[i])

    return answer