def selection_sort(arr, n):
    for i in range(n-1, 0, -1): # 배열의 끝에서 앞으로 감소하며 반복
        max_idx = 0
        for j in range(1, i+1):
            if arr[j] > arr[max_idx]:
                max_idx = j
        arr[max_idx], arr[i] = arr[i], arr[max_idx]

arr = [3, 4, 1, 2]
n = len(arr)
selection_sort(arr, n)
print(arr)
