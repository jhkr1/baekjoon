a = int(input())
b = int(input())
c = int(input())

count = [0] * 10 


result = str(a * b * c)


# for i in range(len(result)): # 0~7 8번 반복
#     for j in range(10): # 0~9까지 10번 반복
#         # 문제점 발생 -> result는 str타입, j는 정수타입이므로 항상 False
#         if(result[i] == j): # result[0] == 0 result[0] == 1 ..
#             count[j] += 1
        
# for k in range(10):
#     print(count[k])


for i in result: 
    num = int(i)
    count[num] += 1
for k in range(10):
    print(count[k])