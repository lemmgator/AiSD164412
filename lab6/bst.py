from typing import Any, List
from graphviz import Digraph


class BinaryNode:
    value: Any
    left_child: 'BinaryNode'
    right_child: 'BinaryNode'

    def __init__(self, value: Any) -> None:
        self.value = value
        self.left_child = None
        self.right_child = None

    def min(self) -> 'BinaryNode':
        if self.left_child:
            return self.left_child.min()
        return self

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


class BinarySearchTree:
    root: BinaryNode

    def __init__(self, root) -> None:
        self.root = root

    def insert(self, value: Any) -> None:
        if self.contains(value):
            return
        self.root = self._insert(self.root, value)

    def _insert(self, node: BinaryNode, value: Any) -> BinaryNode:
        if node:
            if value < node.value:
                node.left_child = self._insert(node.left_child, value)
            else:
                node.right_child = self._insert(node.right_child, value)
        else:
            node = BinaryNode(value)
        return node

    def insert_list(self, list_: List[Any]) -> None:
        for i in list_:
            self.insert(i)

    def contains(self, value: Any) -> bool:
        temp = self.root
        while temp:
            if value == temp.value:
                return True
            if value < temp.value:
                temp = temp.left_child
            else:
                temp = temp.right_child
        return False

    def remove(self, value: Any) -> None:
        if self.contains(value):
            self.root = self._remove(self.root, value)

    def _remove(self, node: BinaryNode, value: Any) -> BinaryNode:
        if value == node.value:
            if node.left_child and node.right_child:
                node.value = node.right_child.min().value
                node.right_child = self._remove(node.right_child, node.right_child.min().value)
            elif node.left_child:
                node = node.left_child
            elif node.right_child:
                node = node.right_child
            else:
                if node == self.root:
                    node.value = 0
                    return node
                node = None
        elif value < node.value:
            node.left_child = self._remove(node.left_child, value)
        else:
            node.right_child = self._remove(node.right_child, value)
        return node

    def show(self) -> None:
        self.root.show().render(filename='binarysearchtree', format='png', cleanup=True, view=False)
