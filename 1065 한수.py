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



