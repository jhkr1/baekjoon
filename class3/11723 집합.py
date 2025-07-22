import sys
def set_command(new_set :set, command:str, num:int):
    if command == "add":
        new_set.add(num)
    elif command == "remove":
        if (num in new_set):
            new_set.remove(num)
    elif command == "check":
        if (num in new_set):
            print(1)
        else:
            print(0)
    elif command == "toggle":
        if (num in new_set):
            new_set.remove(num)
        else:
            new_set.add(num)
    elif command == 'all':
        new_set.clear()
        for i in range(1, 21):
            new_set.add(i)
    elif command == "empty":
        new_set.clear()

n = int(sys.stdin.readline())
new_set = set()

for i in range(n):
    line = sys.stdin.readline().split()
    if len(line) == 1:
        command = line[0]
        num = None
    else:
        command, num = line[0], int(line[1])
    set_command(new_set, command, num)
import sys
def set_command(new_set :set, command:str, num:int):
    if command == "add":
        new_set.add(num)
    elif command == "remove":
        if (num in new_set):
            new_set.remove(num)
    elif command == "check":
        if (num in new_set):
            print(1)
        else:
            print(0)
    elif command == "toggle":
        if (num in new_set):
            new_set.remove(num)
        else:
            new_set.add(num)
    elif command == 'all':
        new_set.clear()
        for i in range(1, 21):
            new_set.add(i)
    elif command == "empty":
        new_set.clear()

n = int(sys.stdin.readline())
new_set = set()

for i in range(n):
    line = sys.stdin.readline().split()
    if len(line) == 1:
        command = line[0]
        num = None
    else:
        command, num = line[0], int(line[1])
    set_command(new_set, command, num)
