def solution(s):
    p_num = s.count('p')
    P_num = s.count('P')
    y_num = s.count('y')
    Y_num = s.count('Y')
    
    return True if p_num + P_num == y_num + Y_num else False