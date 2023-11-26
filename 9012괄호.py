# 내가 생각하는 문제 풀이 스택에 넣어서 "(" 만나면 푸쉬 ")" 만나면 pop
# 만약 스택에 원소가 남아있다면 NO 남아있지않다면 YES

t = int(input())

for i in range(t):
    isVPS = True
    list1 = []
    for ch in input():
        if ch == '(':
            list1.append(ch)
        else:
            if list1:
                 list1.pop()
            else:
                isVPS = False
                break
    if list1:
        isVPS = False
    
    
    print('YES' if isVPS else 'NO')



