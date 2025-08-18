def solution(n, control):
    answer = 0
    for i in range(len(control)):
        if control[i] == "w":
            n += 1
        elif control[i] == "a":
            n -= 10
        elif control[i] == "s":
            n -= 1
        elif control[i] == "d":
            n += 10
    answer = n
    return answer