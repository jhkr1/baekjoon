while True:
    n = int(input())
    if (n == 0):
        break
    n = str(n)
    # 주어진 문자열과 뒤집힌 문자열이 같은지
    if n == n[::-1]:
        print('yes')
    else:
        print('no')