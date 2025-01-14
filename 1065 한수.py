def is_hansu(num):
    if num < 100:
        return True
    elif 100 <= num < 1000:
        a, b = divmod(num, 100)
        c, d = divmod(b, 10)

        if (a - c == c - d):
            return True
        else:
            return False
    else:
        return False



n = int(input())
cnt = 0
for i in range(1,n+1):
    if(is_hansu(i)):
        cnt += 1
print(cnt)


# 개선된 코드
def is_hansu(num):
    """숫자가 한수인지 확인"""
    digits = list(map(int, str(num)))
    if len(digits) <= 2:
        return True  # 1~99는 모두 한수
    return all(digits[i] - digits[i + 1] == digits[i + 1] - digits[i + 2] for i in range(len(digits) - 2))


n = int(input())
cnt = sum(1 for i in range(1, n + 1) if is_hansu(i))  # 한수인 경우 개수를 합산
print(cnt)


