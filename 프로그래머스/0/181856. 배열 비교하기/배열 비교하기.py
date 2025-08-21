def solution(arr1, arr2):
    if len(arr1) == len(arr2):
        t1 = 0
        t2 = 0
        for i in arr1:
            t1 += i
        for j in arr2:
            t2 += j
        if t1 > t2:
            return 1
        elif t1 == t2:
            return 0
        else:
            return -1
        
    elif len(arr1) > len(arr2):
        return 1
    else:
        return -1
        