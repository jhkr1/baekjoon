lotto = set()
user_num = set()

for i in range(1, 50):
    lotto.add(i)

while(True):
    n = int(input())
    if(n == 0):
        break


    for i in range(n):
        user_lotto = input()
        user_num.update(map(int, user_lotto.split()))

    if(lotto == user_num):
        print('Yes')
    else:
        print('No')

    user_num = set()

    
    





