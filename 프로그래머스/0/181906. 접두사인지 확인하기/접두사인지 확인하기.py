def solution(my_string, is_prefix):
    answer = 0
    compare_list = []
    for i in range(1, len(my_string)+1):
        compare_list.append(my_string[:i])
    if is_prefix in compare_list:
        answer = 1
    else:
        answer = 0
    return answer