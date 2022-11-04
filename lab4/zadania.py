# graphviz 0.20.1


from typing import Any, List, Callable, Union
from lab2 import Queue


class TreeNode:
    value: Any
    children: List['TreeNode']

    def __init__(self, value) -> None:
        self.value = value
        self.children = []

    def is_leaf(self) -> bool:
        if self.children:
            return False
        return True

    def add(self, child: 'TreeNode') -> None:
        self.children.append(child)

    def for_each_deep_first(self, visit: Callable[['TreeNode'], None]) -> None:
        visit(self)
        for i in range(len(self.children)):
            self.children[i].for_each_deep_first(visit)

    def for_each_level_order(self, visit: Callable[['TreeNode'], None]) -> None:
        visit(self)
        for i in range(len(self.children)):
            visit(self.children[i])
        if self.children:
            visit


def print_node(tree: 'TreeNode') -> None:
    print(tree.value)


lisc1 = TreeNode(5)
lisc2 = TreeNode(4)
lisc3 = TreeNode(3)
lisc4 = TreeNode(2)
lisc5 = TreeNode(1)
lisc1.add(lisc2)
lisc1.add(lisc3)
lisc2.add(lisc4)
lisc2.add(lisc5)

print(lisc1.is_leaf())
print(lisc2.is_leaf())
print(lisc3.is_leaf())
print(lisc4.is_leaf())
print(lisc5.is_leaf())
#lisc1.for_each_deep_first(print_node)

lisc1.for_each_level_order(print_node)
