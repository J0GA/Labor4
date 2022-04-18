class LinkedNode:
    def __init__(self, value=None):
        self.value = value
        self.right = None
        self.left = None


# Стек
class Stack:
    def __init__(self):  # инициализация
        self.head = LinkedNode()
        self.size = 0

    def is_empty(self):  # is_empty - определить, пусто ли оно
        return self.size == 0

    def push(self, value):  # push - добавляет элемент в верхнюю часть стека
        if self.size > 0:
            node = LinkedNode(value)
            node.right = self.head
            self.head = node
        else:
            self.head.value = value
        self.size += 1

    def pop(self):  # pop - удаляет элемент в верхней части стека
        if self.is_empty():
            return print("Стек пустой!")
        remove = self.head
        if self.size > 1:
            self.head = remove.right
        self.size -= 1
        return remove.value

    def peek(self):  # peek - возвращается к верхнему элементу стека
        if self.is_empty():
            return print("Стек пустой!")
        return self.head.value

    def __len__(self):  # возвращает количество элементов в стеке
        return self.size

    def reverse(self):  # реверс
        current = self.head
        prev = None
        next = None

        while current is not None:
            next = current.right
            current.right = prev
            prev = current
            current = next

        self.head = prev


# Дек
class Deque:
    def __init__(self):  # инициализация
        self.head = LinkedNode()
        self.tail = self.head
        self.size = 0

    def is_empty(self):  # is_empty - определить, пусто ли оно
        return self.size == 0

    def push_left(self, value):  # добавляет к началу двухсторонней очереди
        if self.size > 0:
            node = LinkedNode(value)
            node.right = self.tail
            self.tail.left = node
            self.tail = node
        else:
            self.tail.value = value
        self.size += 1

    def push(self, value):  # добавляет к концу двухсторонней очереди
        if self.size > 0:
            node = LinkedNode(value)
            node.left = self.head
            self.head.right = node
            self.head = node
        else:
            self.head.value = value
        self.size += 1

    def pop_left(self):  # удаляет и возвращает элемент с левой стороны двусторонней очереди
        if self.is_empty():
            return print("Стек пустой!")
        remove = self.tail
        if self.size > 1:
            self.tail = remove.right
        self.size -= 1
        return remove.value

    def pop(self):  # удаляет и возвращает элемент с правой стороны двусторонней очереди
        if self.is_empty():
            return print("Стек пустой!")
        remove = self.head
        if self.size > 1:
            self.head = remove.left
        self.size -= 1
        return remove.value

    def peek(self):  # возвращает элемент начала, не удаляя его
        if self.is_empty():
            return print("Стек пустой!")
        return self.head.value

    def peek_left(self):  # возвращает элемент начала, не удаляя его
        if self.is_empty():
            return print("Стек пустой!")
        return self.tail.value

    def __len__(self):  # возвращает количество элементов в двухсторонней очереди
        return self.size


print("Задание №1")
with open('books.txt','r') as books:
    books=open('books.txt','r', encoding="utf8")
    q1 = Deque()
    q2 = Deque()
    for book in books:
        q1.push(book)
    while not q1.is_empty():
        x = q1.pop()
        while not q2.is_empty() and q2.peek() > x:
            q1.push_left(q2.pop())
        q2.push(x)
    while not q2.is_empty():
        print(q2.pop())