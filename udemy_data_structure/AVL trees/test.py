class Node:
    def __init__(self, data, parent):
        self.data = data
        self.left_node = None
        self.right_node = None
        self.parent = parent
        self.height = 0


class avl:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root is None:
            self.root = Node(data, None)
        else:
            self.insert_node(data, self.root)

    def insert_node(self, data, node):
        if node.data < data:
            if node.left_node:
                self.insert_node(data, node.left_node)
            else:
                node.left_node = Node(data, node)
                node.height = max(self.calculate_height(node.left_node),
                                  self.calculate_height(node.right_node)) + 1
        else:
            if node.right_node:
                self.insert_node(data, node.right_node)
            else:
                node.right_node = Node(data, node)
                node.height = max(self.calculate_height(node.left_node),
                                  self.calculate_height(node.right_node)) + 1
        self.handle_violation(node)

    def calculate_height(self, node):
        if node is None:
            return -1
        return node.height

    def calculate_balance(self, node):
        if node is None:
            return 0

        return self.calculate_height(node.left_node) - self.calculate_height(node.right_node)

    def handle_violation(self, node):
        while node is not None:
            node.height = max(self.calculate_height(node.left_node),
                              self.calculate_height(node.right_node)) + 1
            self.violation_helper(node)
            node = node.parent

    def violation_helper(self, node):
        balance = self.calculate_balance(node)
        if balance > 1:
            if self.calculate_balance(node.left_node) < 0:
                self.rotate_left(node.left_node)
            self.rotate_right(node)
        if balance < -1:
            if self.calculate_balance(node.right_node):
                self.rotate_right(node.right_node)
            self.rotate_left(node)

    def rotate_right(self, node):
        temp_left_node = node.left_node
        t = temp_left_node.right_node

        if t is not None:
            t.parent = node
        temp_parent = node.parent
        node.parent = temp_left_node
        temp_left_node.parent = temp_parent

        if temp_left_node.parent is not None and temp_left_node.parent.left_node == node:
            temp_left_node.parent.left_node = temp_left_node
        if temp_left_node.parent is not None and temp_left_node.parent.right_node == node:
            temp_left_node.parent.right_node = temp_left_node
        if node == self.root:
            self.root = temp_left_node

        node.height = max(self.calculate_height(node.left_node),
                          self.calculate_height(node.right_node)) + 1
        temp_left_node.height = max(self.calculate_height(temp_left_node.left_node),
                                    self.calculate_height(temp_left_node.right_node)) + 1

    def rotate_left(self, node):
        temp_right_node = node.right_node
        t = temp_right_node.left_node
        if t is not None:
            t.parent = node
        temp_parent = node.parent
        node.parent = temp_right_node
        temp_right_node.parent = temp_parent

        if temp_right_node.parent is not None and temp_right_node.parent.left_node == node:
            temp_right_node.parent.left_node = temp_right_node
        if temp_right_node.parent is not None and temp_right_node.parent.right_node == node:
            temp_right_node.parent.right_node = temp_right_node
        if node == self.root:
            temp_right_node = self.root
        node.height = max(calculate_height(node.left_node), calculate_height(node.right_node)) + 1
        temp_right_node.height = max(calculate_height(
            temp_right_node.left_node), calculate_height(temp_right_node.right_node)) + 1

    def remove(self, data):
        if self.root:
            self.remove_node(data, self.root)

    def remove_node(self, data, node):
        if node is None:
            return
        if data < node.data:
            self.remove_node(data, node.left_node)
        if data > node.data:
            self.remove_node(data, node.right_node)
        else:
            if node.left_node is None and node.right_node is None:
                parent = node.parent
                if parent is not None and parent.left_node == node:
                    parent.left_node = None
                if parent is not None and parent.right_node == node:
                    parent.right_node = None
                if parent == None:
                    self.root = None
                del node
                self.handle_violation(parent)

            elif node.left_node is None and node.right_node is not None:
                parent = node.parent
                if parent is not None:
                    if parent.left_node == node:
                        parent.left_node = node.right_node
                    if parent.right_node == node:
                        parent.right_node = node.right_node
                else:
                    self.root = None

                node.right_node.parent = parent

                del node
                self.handle_violation(parent)
            elif node.left_node is not None and node.right_node is None:
                parent = node.parent
                if parent is not None:
                    if parent.left_node == node:
                        parent.left_node = node.left_node
                    if parent.right_node == node:
                        parent.right_node = node.left_node
                if parent is None:
                    self.root = None
                node.right_node.parent = parent
                del node
                self, handle_violation(parent)
            elif node.left_node is not None and node.right_node is not None:
                predecessor = self.get_predecessor(node.left_node)
                temp = predecessor.data
                predcessor.data = node.data
                node.data = temp
                self.remove_node(data, predecessor)

    def get_predecessor(self, node):
        if node.right_node:
            self.get_predecessor(node.right_node)


avl = avl()
avl.insert(10)
avl.insert(5)
avl.insert(14)
avl.insert(11)
avl.insert(16)
avl.insert(7)
