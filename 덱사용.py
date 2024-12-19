from collections import deque

n = int(input())
dq = deque()

for i in range(n):
    command = input().split()
    
    if (command[0] == 'push_front'):
        val = command[1]
        dq.appendleft(val)
    
    elif (command[0] == 'push_back'):
        val = command[1]
        dq.append(val)
    
    elif (command[0] == 'pop_front'):
        print(dq.popleft())
    
    elif (command[0] == 'pop_back'):
        print(dq.pop())
    
    elif (command[0] == 'size'):
        print(len(dq))
    
    elif (command[0] == 'empty'):
        print(1 if not dq else 0)
    
    elif (command[0] == 'front'):
        if dq:
            print(dq[0])
        else:
            raise("deque is empty")
    
    elif (command[0] == 'back'):
        if dq:
            print(dq[-1])
        else:
            raise("deque is empty")
        
