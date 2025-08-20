def solution(arr):
    arr_zero = [[0]*len(arr[0]) for _ in range(len(arr))]
    for i in range(len(arr)):
        for j in range(len(arr)):
            arr_zero[j][i] = arr[i][j]
    if arr_zero == arr:
        return 1
    else:
        return 0