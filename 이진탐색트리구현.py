class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def search(self, x):
        node = self.root
        while node is not None and node.value != x:
            if node.value > x:
                node = node.left
            else:
                node = node.right
        return node

    def minimum(self, node):
        while node.left is not None:
            node = node.left
        return node

    def delete(self, x):
        node = self.search(x)
        if node is None:
            return None

        def transplant(u, v):
            if u.parent is None:
                self.root = v
            elif u == u.parent.left:
                u.parent.left = v
            else:
                u.parent.right = v
            if v is not None:
                v.parent = u.parent

        # Case 1: Node has no left child
        if node.left is None:
            transplant(node, node.right)
        # Case 2: Node has no right child
        elif node.right is None:
            transplant(node, node.left)
        else:
            # Case 3: Node has two children
            succ = self.minimum(node.right)
            if succ.parent != node:
                transplant(succ, succ.right)
                succ.right = node.right
                succ.right.parent = succ
            transplant(node, succ)
            succ.left = node.left
            succ.left.parent = succ

    def insert(self, x):
        node = TreeNode(x)
        y = None
        temp = self.root
        while temp is not None:
            y = temp
            if node.value < temp.value:
                temp = temp.left
            else:
                temp = temp.right
        node.parent = y
        if y is None:
            self.root = node
        elif node.value < y.value:
            y.left = node
        else:
            y.right = node

# 사용 예시
bst = BinarySearchTree()
bst.insert(8)
bst.insert(3)
bst.insert(10)
bst.insert(1)
bst.insert(6)
bst.insert(14)
bst.insert(4)
bst.insert(7)
bst.insert(13)

# 노드 삭제 예시
bst.delete(10)