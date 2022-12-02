from typing import Any, Callable
from graphviz import *


class BinaryNode:
    value: Any
    left_child: 'BinaryNode'
    right_child: 'BinaryNode'

    def __init__(self, value: Any) -> None:
        self.value = value
        self.left_child = None
        self.right_child = None

    def is_leaf(self) -> bool:
        if self.left_child or self.right_child:
            return False
        return True

    def add_left_child(self, value: Any) -> None:
        if self.left_child:
            print('Node już zawiera lewe dziecko.')
            return
        self.left_child = BinaryNode(value)

    def add_right_child(self, value: Any) -> None:
        if self.right_child:
            print('Node już zawiera prawe dziecko.')
            return
        self.right_child = BinaryNode(value)

    def traverse_in_order(self, visit: Callable[[Any], None]) -> None:
        if self.left_child:
            self.left_child.traverse_in_order(visit)
        visit(self)
        if self.right_child:
            self.right_child.traverse_in_order(visit)

    def traverse_post_order(self, visit: Callable[[Any], None]) -> None:
        if self.left_child:
            self.left_child.traverse_post_order(visit)
        if self.right_child:
            self.right_child.traverse_post_order(visit)
        visit(self)

    def traverse_pre_order(self, visit: Callable[[Any], None]) -> None:
        visit(self)
        if self.left_child:
            self.left_child.traverse_pre_order(visit)
        if self.right_child:
            self.right_child.traverse_pre_order(visit)

    def show(self, g=Digraph('g')):
        g.node(str(self), str(self.value))
        if self.left_child:
            g.edge(str(self), str(self.left_child))
            self.left_child.show(g)
        if self.right_child:
            g.edge(str(self), str(self.right_child))
            self.right_child.show(g)
        return g

    def __str__(self) -> str:
        return str(self.value)


class BinaryTree:
    root: BinaryNode

    def __init__(self, root: BinaryNode) -> None:
        self.root = root

    def traverse_in_order(self, visit: Callable[[Any], None]) -> None:
        self.root.traverse_in_order(visit)

    def traverse_pre_order(self, visit: Callable[[Any], None]) -> None:
        self.root.traverse_pre_order(visit)

    def traverse_post_order(self, visit: Callable[[Any], None]) -> None:
        self.root.traverse_post_order(visit)

    def show(self) -> None:
        self.root.show().render(filename='binarytree', format='png', cleanup=True, view=True)
