def solution(n):
    answer = []
    i = 1
    while n > i:
        if n % i == 1:
            answer.append(i)
        i += 1
    answer.sort()
    return answer[0]