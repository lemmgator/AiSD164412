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

# 2)


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


# 3)


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


# wywołania zadanie 1

list_ = LinkedList()
assert list_.head is None

list_.push(1)
list_.push(0)
assert str(list_) == '0 -> 1'

list_.append(9)
list_.append(10)
assert str(list_) == '0 -> 1 -> 9 -> 10'

middle_node = list_.node(at=1)
list_.insert(5, after=middle_node)
assert str(list_) == '0 -> 1 -> 5 -> 9 -> 10'

first_element = list_.node(at=0)
returned_first_element = list_.pop()
assert first_element == returned_first_element

last_element = list_.node(at=3)
returned_last_element = list_.remove_last()
assert last_element == returned_last_element


# wywołania zadanie 2

stack = Stack()
assert len(stack) == 0

stack.push(3)
stack.push(10)
stack.push(1)
assert len(stack) == 3

top_value = stack.pop().value
assert top_value == 1
assert len(stack) == 2

print(str(stack))


# wywołania zadanie 3

queue = Queue()
assert len(queue) == 0

queue.enqueue('klient1')
queue.enqueue('klient2')
queue.enqueue('klient3')
assert str(queue) == 'klient1, klient2, klient3'

client_first = queue.dequeue().value
assert client_first == 'klient1'
assert str(queue) == 'klient2, klient3'
assert len(queue) == 2
