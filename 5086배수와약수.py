# 각 테스트 케이스마다 
# 첫 번째 숫자가 두 번째 숫자의 약수라면 factor를
# 배수라면 multiple을, 둘 다 아니라면 neither

while True:
    a, b = map(int, input().split())
    if(a == 0 & b == 0):
        break
    else:
        # 약수인 경우
        if (b % a == 0):
            print('factor')
        # 배수인 경우
        elif (a % b == 0):
            print('multiple')
        # 둘다 아닌 경우
        else:
            print('neither')
