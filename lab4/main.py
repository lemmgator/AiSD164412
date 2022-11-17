from tree import *


def main():
    treenode = TreeNode('F')
    treenode.add(TreeNode('B'))
    treenode.add(TreeNode('G'))
    treenode.children[0].add(TreeNode('A'))
    treenode.children[0].add(TreeNode('D'))

    tree = Tree(treenode)
    tree.add('C', tree.root.children[0].children[1])
    tree.add('E', tree.root.children[0].children[1])
    tree.add('I', tree.root.search('G'))
    tree.add('H', tree.root.search('I'))

    print(tree.root.is_leaf())
    print(tree.root.search('H').is_leaf())
    print(tree.root.search('Z'))
    tree.for_each_deep_first(print_node)
    print('~')
    tree.for_each_level_order(print_node)
    tree.show()


if __name__ == '__main__':
    main()
