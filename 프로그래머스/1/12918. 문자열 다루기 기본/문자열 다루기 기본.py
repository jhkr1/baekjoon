def solution(s):
    # 문자열 s의 길이는 4 or 6이고 숫자로만 구성되어있는지.
    return True if (len(s) == 4 or len(s) == 6)and s.isdigit() else False