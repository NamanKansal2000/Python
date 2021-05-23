class Node:
    def __init__(self, data, parent):
        self.data = data
        self.leftChild = None
        self.rightChild = None
        self.parent = parent


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, root, data):
        if self.root is None:
            self.root = Node(data, None)
        else:
            self.insert_node(self.root, data)

    def insert_node(self, node, data):
        if data < node.data:
            if node.leftChild is not None:
                self.insert_node(data, node.leftChild)
            else:
                node.leftChild = Node(data, node)

        else:
            if node.rightChild is not None:
                self.insert_node(data, node.rightChild)
            else:
                self.rightChild = Node(data, node)

    def traverse(self, root):
        if self.root is not None:
            self.traverse_in_order(self.root)

    def traverse_in_order(self, node):
        if node.leftChild is not None:
            traverse_in_order(node.leftChild)
        print(node.data, " > ")
        if node.rightChild is not None:
            traverse_in_order(node.rightChild)

    def get_max_value(self, root):
        if self.root is not None:
            self.get_max(self.root)
        return "No binary tree/ vaue exists"
    def get_max(self, node):
        if node.rightChild is not None:
            self.get_max(node.rightChild)
        print(node.data)

    def get_min_value(self, root):
        if self.root is not None:
            self.get_min(self.root)
        return "No binary tree/ vaue exists"
    def get_min(self, node):
        if node.leftChild is not None:
            self.min_value(node.leftChild)
        print(node.data)

    def height(self, root):
        if self.root is not None:
            self.height_tree(self.root)
        return 0
    def height_tree(self, node):
        ldepth = height_tree(node.leftChild)
        rdepth = height_tree(node.rightChild)

        if ldepth > rdepth:
            return (1+ldepth)
        else:
            return (1+rdepth)

    def remove(self, root, data):
        if self.root is not None:
            self.remove_node(self.root, data)
    def remove_node(self, node, data):
        if node is None:
            return
        if data < node.data:
            self.remove_node(node.leftChild, data)
        if data > node.data:
            self.remove_node(node.rightChild, data)
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
