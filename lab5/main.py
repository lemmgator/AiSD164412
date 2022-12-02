from binarytree import *


def main():
    node = BinaryNode(10)
    node.add_left_child(9)
    node.left_child.add_left_child(1)
    node.left_child.add_right_child(3)
    node.add_right_child(2)
    node.right_child.add_left_child(4)
    node.right_child.add_right_child(6)
    tree = BinaryTree(node)

    tree.traverse_in_order(print)
    print('~')
    tree.traverse_post_order(print)
    print('~')
    tree.traverse_pre_order(print)
    tree.show()

    assert tree.root.value == 10
    assert tree.root.right_child.value == 2
    assert tree.root.right_child.is_leaf() is False
    assert tree.root.left_child.left_child.value == 1
    assert tree.root.left_child.left_child.is_leaf() is True


if __name__ == '__main__':
    main()
