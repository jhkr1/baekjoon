# 몸무게 x, 키가 y라면 덩치는 (x, y)
# 두사람 A와 B의 덩치가 각각 (x, y), (p, q)
num = int(input())
total_list = []
rank_list = [1] * num

for i in range(num):
    a, b = map(int, input().split())
    total_list.append((a, b))

# 몸무게와 키를 동시에 비교해야함.
for i in range(num):
    for j in range(num):
        if i != j:
            if total_list[i][0] < total_list[j][0] and total_list[i][1] < total_list[j][1]:
                rank_list[i] += 1


    



    



    

