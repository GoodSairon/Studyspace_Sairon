from tree import Node, Tree

a = [3, 4, 2, 5, 1]
tree = Tree()
for i in a:
        tree.append(Node(i))

def test_append():

    assert tree.root.data == 3
    assert tree.root.left.data == 2
    assert tree.root.left.left.data == 1
    assert tree.root.right.data == 4
    assert tree.root.right.right.data == 5

    return print("Append test: Done")

def test_min_max():

    assert tree.find_min() == 1
    assert tree.find_max() == 5

    return print("Min Max test: Done")

test_append()
test_min_max()
