def solution(n):
    i = 1
    answer = 0
    while n >= i:
        if (n % i == 0):
            answer += i
        i += 1
    return answer