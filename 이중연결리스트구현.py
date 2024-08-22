# Node 클래스
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

# 이중 연결 리스트 클래스
class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.node_num = 0

    def push_front(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head

        if self.head != None:  # 기존 리스트가 비어있지 않다면
            self.head.prev = new_node
            self.head = new_node
            new_node.prev = None
        else:  # 기존 리스트가 비어있다면
            self.head = new_node
            self.tail = new_node
            new_node.prev = None

        self.node_num += 1

    def push_back(self, new_data):
        new_node = Node(new_data)
        new_node.prev = self.tail

        if self.tail != None:  # 기존 리스트가 비어있지 않다면
            self.tail.next = new_node
            self.tail = new_node
            new_node.next = None
        else:  # 기존 리스트가 비어있다면
            self.head = new_node
            self.tail = new_node
            new_node.next = None
        self.node_num += 1

    def pop_front(self):
        if self.head == None:
            print("List is Empty")
            return None
        elif self.head.next == None:  # 노드가 하나 남았다면
            temp = self.head

            self.head = None
            self.tail = None
            self.node_num = 0
            return temp.data
        else:  # 노드의 개수가 여러개 일때
            temp = self.head
            temp.next.prev = None
            self.head = temp.next
            temp.next = None

            self.node_num -= 1
            return temp.data

    def pop_back(self):
        if self.tail == None:  # 노드가 없다면
            print("List is Empty")
            return None
        elif self.tail.prev == None:  # 노드가 1개만 남았다면
            temp = self.tail

            self.head = None
            self.tail = None
            self.node_num = 0
            return temp.data
        else:  # 노드가 여러 개 남았을 경우
            temp = self.tail
            temp.prev.next = None
            self.tail = temp.prev
            self.node_num -= 1
            return temp.data

    def size(self):
        return self.node_num

    def empty(self):
        if self.node_num == 0:
            print(1)
        else:
            print(0)

    def front(self):
        if self.head == None:
            print("List is Empty")
        else:
            return self.head.data

    def back(self):
        if self.tail == None:
            print("List is Empty")
        else:
            return self.tail.data


# 연결 리스트 객체 생성
dll = DoublyLinkedList()

N = int(input())
for i in range(N):
    temp = input().split()
    command = temp[0]

    if command == 'push_back':
        vals = int(temp[1])
        dll.push_back(vals)

    elif command == 'push_front':
        vals = int(temp[1])
        dll.push_front(vals)

    elif command == 'pop_front':
        print(dll.pop_front())

    elif command == 'pop_back':
        print(dll.pop_back())

    elif command == 'size':
        print(dll.size())

    elif command == 'empty':
        dll.empty()

    elif command == 'front':
        print(dll.front())
        
    elif command == 'back':
        print(dll.back())