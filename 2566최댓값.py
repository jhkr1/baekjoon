rows, cols = 9, 9
arr = []
for i in range(rows):
    arr.append(list(map(int, input().split())))

# for i in arr:
#     print(i)

# 1행에서 최댓값 max1 -> 2행에서 최댓값 max2 .... 9행에서 최댓값 max9 중 가장 큰 값을 result에 저장
max_arr = []
max_rows = 0
max_cols = 0

for i in arr:
    # 한 행마다 가장 큰 값을 max_arr에 추가
    max_arr.append(max(i))
    
result = max(max_arr)

print(result)

for i in range(rows):
    for j in range(cols):
        if (arr[i][j] == result):
            max_rows = i+1
            max_cols = j+1

print(max_rows, max_cols)
