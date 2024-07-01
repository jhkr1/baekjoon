# 1. 처음 입력받은 2가지 숫자로 N*M 행렬을 만든다
# 2. N*M 행렬을 하나 더 만든다.
# 3. 출력: 처음 만든 행렬과 두 번째로 만든 행렬을 더한 후 출력한다.

temp = input().split()
rows, cols = int(temp[0]), int(temp[1])
# print(n, m)

# 첫 번째 배열 
array1 = [input().split() for _ in range(rows)]
# 두 번째 배열
array2 = [input().split() for _ in range(rows)]
array3 = [[0] * cols for _ in range(rows)]


# print(int(array1[0][0]) + int(array2[0][0]))

for i in range(rows):
    for j in range(cols):
        array3[i][j] = (int(array1[i][j]) + int(array2[i][j]))

for i in range(rows):
    for j in range(cols):
        print(array3[i][j], end=' ')
    print()
        
# 개선된 코드
rows, cols = map(int, input().split())

arr1 = []
for _ in range(rows):
    arr1.append(list(map(int, input().split())))

arr2 = []
for _ in range(rows):
    arr2.append(list(map(int, input().split())))

arr3 = [[0] * cols for _ in range(rows)]

for i in range(rows):
    for j in range(cols):
        arr3[i][j] = arr1[i][j] + arr2[i][j]

for i in range(rows):
    for j in range(cols):
        print(arr3[i][j], end=' ')
    print()