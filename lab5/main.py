from binarytree import *


def main():
    binarynode = BinaryNode(10)
    binarynode.add_left_child(9)
    binarynode.left_child.add_left_child(1)
    binarynode.left_child.add_right_child(3)
    binarynode.add_right_child(2)
    binarynode.right_child.add_left_child(4)
    binarynode.right_child.add_right_child(6)
    tree = BinaryTree(binarynode)

    tree.traverse_in_order(print)
    print('~')
    tree.traverse_post_order(print)
    print('~')
    tree.traverse_pre_order(print)

    assert tree.root.value == 10
    assert tree.root.right_child.value == 2
    assert tree.root.right_child.is_leaf() is False
    assert tree.root.left_child.left_child.value == 1
    assert tree.root.left_child.left_child.is_leaf() is True


if __name__ == '__main__':
    main()
