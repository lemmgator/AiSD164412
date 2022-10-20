# 1)

from typing import Any


class Node:
    value: Any
    next: 'Node'

    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    head: Node
    tail: Node

    def __init__(self):
        self.head = None
        self.tail = None

    def push(self, value: Any) -> None:
        if self.head is None:
            self.head = Node(value)
            self.tail = self.head
        else:
            temp = self.head
            self.head = Node(value)
            self.head.next = temp

    def append(self, value: Any) -> None:
        if self.head is None:
            self.head = Node(value)
            self.tail = self.head
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            self.tail = Node(value)
            temp.next = self.tail

    def node(self, at: int) -> Node:
        temp = self.head
        for i in range(at):
            temp = temp.next
        return temp

    def insert(self, value: Any, after: Node) -> None:
        if after is None:
            print("ale lipa!!!")
            return

        temp = Node(value)
        temp.next = after.next
        after.next = temp

    def pop(self) -> Any:
        val = self.head.value
        self.head = self.head.next
        return val

    def remove_last(self) -> Any:
        val = self.tail.value
        temp = self.head
        while temp.next is not self.tail:
            temp = temp.next
        temp.next = None
        return val

    def remove(self, after: Node) -> None:
        if after is None:
            print("ale lipa!!!")
            return

        temp = self.head
        while temp.next is not after:
            temp = temp.next
        temp.next = after.next

    def print(self) -> None:
        temp = self.head
        while temp.next:
            print(temp.value, end=" -> ")
            temp = temp.next
        print(temp.value)

    def len(self) -> int:
        if self.head is None:
            return 0
        w = 1
        temp = self.head
        while temp.next:
            w += 1
            temp = temp.next
        return w


lista1 = LinkedList()
lista1.push(1)
lista1.push(0)
lista1.append(9)
lista1.append(10)
lista1.insert(5, after=lista1.node(at=1))

lista1.print()
print(lista1.len())

first_element = lista1.node(at=0)
returned_first_element = lista1.pop()
assert first_element.value == returned_first_element

last_element = lista1.node(at=3)
returned_last_element = lista1.remove_last()
assert last_element.value == returned_last_element

lista1.remove(after=lista1.node(at=2))

lista1.print()
print(lista1.len())
