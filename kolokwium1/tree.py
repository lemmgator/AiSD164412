from typing import Any, List, Callable, Union
from queue import Queue
from graphviz import *


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
        for i in self.children:
            i.for_each_deep_first(visit)

    def for_each_level_order(self, visit: Callable[['TreeNode'], None]) -> None:
        q = Queue()
        q.enqueue(self)
        while q:
            visit(q.peek())
            for i in q.peek().children:
                q.enqueue(i)
            q.dequeue()

    def search(self, value: Any) -> Union['TreeNode', None]:
        if self.value == value:
            return self
        for i in self.children:
            w = i.search(value)
            if w:
                return w

    def show(self, g=Digraph('g')):
        g.node(str(self), str(self.value))
        for i in self.children:
            g.edge(str(self), str(i))
            i.show(g)
        return g


class Tree:
    root: TreeNode

    def __init__(self, root) -> None:
        self.root = root

    def add(self, value: Any, parent_name: Any) -> None:
        parent_name.children.append(TreeNode(value))

    def for_each_level_order(self, visit: Callable[['TreeNode'], None]) -> None:
        self.root.for_each_level_order(visit)

    def for_each_deep_first(self, visit: Callable[['TreeNode'], None]) -> None:
        self.root.for_each_deep_first(visit)

    def show(self) -> None:
        self.root.show().render(filename='tree', format='png', cleanup=True, view=True)


def print_node(tree: 'TreeNode') -> None:
    if isinstance(tree, TreeNode):
        print(tree.value)
    else:
        print(tree)
