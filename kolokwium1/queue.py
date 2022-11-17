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
        temp = self.head
        self.head = Node(value)
        self.head.next = temp
        if temp is None:
            self.tail = self.head

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
        temp = self.head
        self.head = self.head.next
        return temp

    def remove_last(self) -> Any:
        temp = self.head
        while temp.next is not self.tail:
            temp = temp.next
        w = temp.next
        temp.next = None
        self.tail = temp
        return w

    def remove(self, after: Node) -> None:
        after.next = after.next.next

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


class Stack:
    storage: LinkedList

    def __init__(self):
        self.storage = LinkedList()

    def push(self, element: Any):
        self.storage.push(element)

    def pop(self) -> Any:
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
