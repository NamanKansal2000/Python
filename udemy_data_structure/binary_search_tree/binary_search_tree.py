class Node:
    def __init__(self, data, parent):
        self.data = data
        self.leftChild = None
        self.rightChild = None
        self.parent = parent


class BinarySearchTree:

    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root is None:
            self.root = Node(data, None)
        else:
            self.insert_node(data, self.root)

    def insert_node(self, data, node):
        # left sub tree
        if data < node.data:
            if node.leftChild is not None:
                self.insert_node(data, node.leftChild)
            else:
                node.leftChild = Node(data, node)
        # right sub tree
        else:
            if node.rightChild is not None:
                self.insert_node(data, node.rightChild)
            else:
                node.rightChild = Node(data, node)

    def traverse(self):
        if self.root is not None:
            self.traverse_in_order(self.root)

    def traverse_in_order(self, node):
        if node.leftChild:
            self.traverse_in_order(node.leftChild)
        print(node.data, end=">")
        if node.rightChild:
            self.traverse_in_order(node.rightChild)

    def get_max_value(self):
        if self.root:
            self.get_max(self.root)

    def get_max(self, node):
        if node.rightChild:
            return self.get_max(node.rightChild)
        return node.data

    def get_min_value(self):
        if self.root:
            self.get_min(self.root)

    def get_min(self, node):
        if node.leftChild:
            return self.get_min(node.leftChild)
        return node.data

    def remove(self, data):
        if self.root is not None:
            self.remove_node(data, self.root)

    def remove_node(self, data, node):
        if node is None:
            return
        if data < node.data:
            self.remove_node(data, node.leftChild)
        if data > node.data:
            self.remove_node(data, node.rightChild)
        else:
            if node.rightChild is None and node.leftChild is None:
                parent = node.parent

                if parent is not None and parent.leftChild == node:
                    parent.leftChild = None
                if parent is not None and parent.rightChild == node:
                    parent.rightChild = None
                if parent is None:
                    self.root = None
                del node
            elif node.leftChild is not None and node.rightChild is None:
                parent = node.parent
                if parent is not None and parent.leftChild == node:
                    parent.leftChild = node.leftChild
                if parent is not None and parent.rightChild == node:
                    parent.rightChild = node.leftChild
                if parent is None:
                    self.root = None
                node.leftChild.parent = parent
                del node

            elif node.leftChild is None and node.rightChild is not None:
                parent = node.parent
                if parent is not None and parent.leftChild == node:
                    parent.leftChild = node.rightChild
                if parent is not None and parent.rightChild == node:
                    parent.rightChild = node.rightChild
                if parent is None:
                    self.root = None
                node.rightChild.parent = parent
                del node
            else:
                predecessor = self.get_predecessor(node.leftChild)
                temp = predecessor.data
                predecessor.data = node.data
                node.data = temp
                self.remove_node(data, predecessor)

    def get_predecessor(self, node):
        if node.rightChild:
            return self.get_predecessor(node.rightChild)
        return node


bst = BinarySearchTree()
bst.insert(10)
bst.insert(-5)
bst.insert(-100)
bst.insert(15)
bst.insert(66)
bst.insert(1)
print('Max_value:-', bst.get_max(bst.root))
print('Min_value:-', bst.get_min(bst.root))
bst.traverse()
bst.remove(10)
print()
bst.traverse()
