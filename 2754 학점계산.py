score = input()
result = 0


if score[0] == 'A':
    result = 4
elif score[0] == 'B':
    result = 3
elif score[0] == 'C':
    result = 2
elif score[0] == 'D':
    result = 1
else:
    result = 0

if len(score) > 1:
    if score[1] == '+':
        result += 0.3
    elif score[1] == '-':
        result -= 0.3


print(float(result))