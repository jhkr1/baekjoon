def solution(n):
    result = []
    n = str(n)
    n = n[-1::-1]
    for i in range(len(n)):
        result.append(int(n[i]))
    return result
        