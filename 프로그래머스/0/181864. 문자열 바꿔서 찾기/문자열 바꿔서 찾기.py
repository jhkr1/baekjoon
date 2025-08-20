def solution(myString, pat):
    myString = myString.translate(str.maketrans('AB', 'BA'))  # 문자열 변환
    if pat in myString:
        answer = 1
    else:
        answer = 0
    return answer