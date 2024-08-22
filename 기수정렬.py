def counting_sort_for_radix(arr, exp):
    n = len(arr)
    output = [0] * n
    count = [0] * 10

    # 현재 자릿수의 count 배열 저장
    for i in range(n):
        index = arr[i] // exp
        count[index % 10] += 1

    # count 배열 수정하여 실제 위치 저장
    for i in range(1, 10):
        count[i] += count[i - 1]

    # output 배열 생성
    i = n - 1
    while i >= 0:
        index = arr[i] // exp
        output[count[index % 10] - 1] = arr[i]
        count[index % 10] -= 1
        i -= 1

    # output 배열의 값을 arr에 복사
    for i in range(n):
        arr[i] = output[i]

def radix_sort(arr):
    # arr 중 가장 큰 수 찾기
    max1 = max(arr)

    # 가장 큰 수의 자리수만큼 count_sort 수행
    exp = 1
    while max1 // exp > 0:
        counting_sort_for_radix(arr, exp)
        exp *= 10

# 입력 받기
n = int(input())
arr = list(map(int, input().split()))

# 정렬 수행
radix_sort(arr)

# 출력
for i in range(n):
    print(arr[i], end=' ')