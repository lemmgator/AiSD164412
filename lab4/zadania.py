# graphviz 0.20.1


from typing import Any, List, Callable, Union


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

    def visit(self):
        
    def for_each_deep_first(self, visit: Callable[['TreeNode'], None]) -> None:
        return


lisc1 = TreeNode(5)
lisc2 = TreeNode(4)
lisc3 = TreeNode(3)
lisc1.add(lisc2)
lisc1.add(lisc3)

print(lisc1.is_leaf())
print(lisc2.is_leaf())
print(lisc3.is_leaf())
lisc1.for_each_deep_first()
