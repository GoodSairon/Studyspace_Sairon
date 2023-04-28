class Node:

    def __init__(self, data):

        self.left = None
        self.right = None
        self.data = data

class Tree:

    def __init__(self):
        self.root = None

    def __find(self, node, parent, value):

        if node is None:
            return None, parent, False

        if parent == None:
            parent = self.root

        if value == node.data:
            return node, parent, True

        if value < node.data:
            if node.left:
                return self.__find(node.left, node, value)

        if value > node.data:
            if node.right:
                return self.__find(node.right, node, value)

        return node, parent, False

    def append(self, obj):

        if self.root == None:
            self.root = obj
            return obj

        s, p, fl_find = self.__find(self.root, None, obj.data)

        if not fl_find and s:
            if obj.data < s.data:
                s.left = obj
            else:
                s.right = obj

        return obj

    def __find_min(self, node, parent):

        if node.left:
            return self.__find_min(node.left, node)

        return node, parent

    def find_min(self, node = None):

        if self.root == None:
            return

        if node == None:
            node = self.root

        if node.left:
            return self.find_min(node.left)

        return int(node.data)


    def find_max(self, node = None):

        if self.root == None:
            return

        if node == None:
            node = self.root

        if node.right:
            return self.find_max(node.right)

        return int(node.data)

    def __del_leaf(self, s, p):

        if p.left == s:
            p.left = None
        elif p.right == s:
            p.right = None

    def __del_one_child(self, s, p):

        if p.left == s:
            if s.left is None:
                p.left = s.right
            elif s.right is None:
                p.left = s.left
        elif p.right == s:
            if s.left is None:
                p.right = s.right
            elif s.right is None:
                p.right = s.left

    def del_node(self, key):

        s, p, fl_find = self.__find(self.root, None, key.data)

        if not fl_find:
            return None

        if s.left is None and s.right is None:
            self.__del_leaf(s, p)
        elif s.left is None or s.right is None:
            if  s == p:
                self.root = s.right
            else:
                self.__del_one_child(s, p)
        else:
            sr, pr = self.__find_min(s.right, s)
            s.data = sr.data
            self.__del_one_child(sr, pr)

#In this tree root is minimal value

a = [1, 3, 5, 2, 4, 9, 6]

tree = Tree()

for i in a:
    tree.append(Node(i))

print('min:', tree.find_min())
print('max:', tree.find_max())

print('Delete min')
tree.del_node(Node(tree.find_min()))
print('Delete max')
tree.del_node(Node(tree.find_max()))

print('new min:', tree.find_min())
print('new max:', tree.find_max())

#In this tree root is any value (not minimal)

a = [2, 3, 5, 1, 4, 9, 6]

tree = Tree()

for i in a:
    tree.append(Node(i))

print('min:', tree.find_min())
print('max:', tree.find_max())

print('Delete min')
tree.del_node(Node(tree.find_min()))
print('Delete max')
tree.del_node(Node(tree.find_max()))

print('new min:', tree.find_min())
print('new max:', tree.find_max())

print('Delete root')
tree.del_node(tree.root)

print('new root:', tree.root.data)
