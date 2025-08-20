def solution(arr, delete_list):
    delete_set = set(delete_list)
    return [x for x in arr if x not in delete_set]
