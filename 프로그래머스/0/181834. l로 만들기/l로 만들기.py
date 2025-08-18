def solution(myString):
    answer = ''
    compare = ord('l')
    for i in range(len(myString)):
        if ord(myString[i]) < compare:
            answer += myString[i].replace(myString[i], 'l')
        else:
            answer += myString[i]
    return answer