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

    def __str__(self) -> str:
        w = ''
        if self.head is None:
            return w
        temp = self.head
        w += f'{temp.value}'
        while temp.next:
            temp = temp.next
            w += f' -> {temp.value}'
        return w

    def __len__(self) -> int:
        w = 0
        temp = self.head
        while temp:
            w += 1
            temp = temp.next
        return w


class Queue:
    storage: LinkedList

    def __init__(self):
        self.storage = LinkedList()

    def peek(self) -> Any:
        return self.storage.head.value

    def enqueue(self, element: Any):
        self.storage.append(element)

    def dequeue(self) -> Any:
        return self.storage.pop()

    def __str__(self) -> str:
        w = ''
        if self.storage.head is None:
            return w
        temp = self.storage.head
        w += f'{temp.value}'
        while temp.next:
            temp = temp.next
            w += f', {temp.value}'
        return w

    def __len__(self) -> int:
        w = 0
        temp = self.storage.head
        while temp:
            w += 1
            temp = temp.next
        return w
