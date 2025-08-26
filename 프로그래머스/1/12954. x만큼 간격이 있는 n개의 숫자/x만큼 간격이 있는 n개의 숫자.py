def solution(x, n):
    answer = [0] * n
    for i in range(n):
        if i == 0:
            answer[i] = x
        else:
            answer[i] = x * (i+1)
    return answer