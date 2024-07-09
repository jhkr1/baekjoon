t = int(input())
for _ in range(t):
    temp = input().upper()
    score = 0
    O_list = 0


    for i in range(len(temp)):
        if (temp[i] == 'O'):
            O_list += 1
            score += O_list
        elif (temp[i] == 'X'):
            O_list = 0
            
    print(score)


