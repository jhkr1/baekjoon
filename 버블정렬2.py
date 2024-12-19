def bubble_sort(arr):
    n = len(arr)
    
    for i in range(n):
        for j in range(n-1-i): # 각 단계에서 마지막 i개의 요소는 이미 정렬됨.
            if arr[j] > arr[j+1]:
                arr[j+1], arr[j] = arr[j], arr[j+1]   

arr = [3, 4, 1, 2]
bubble_sort(arr)
print(arr)