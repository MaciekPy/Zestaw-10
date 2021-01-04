
class Stack:

    def __init__(self):
        self.items = []

    def __str__(self):                  # podglądamy stos
        return str(self.items)

    def is_empty(self):
        return not self.items

    def is_full(self):                  # nigdy nie jest pełny
        return False

    def push(self, item):
        if self.is_full():
            raise ValueError("Stos jest pelny")
        return self.items.append(item)         # dodajemy na koniec

    def pop(self):
        if self.is_empty():
            raise ValueError("Stos jest pusty")
        return self.items.pop()
        # zabieram od końca


stack1 = Stack()
print("is Empty? :")
print(stack1.is_empty())
stack1.push(1)
stack1.push(2)
stack1.push(3)
print(stack1)
print("is Full? :")
print(stack1.is_full())
stack1.pop()
print(stack1)
stack1.pop()
print(stack1)
stack1.pop()
print(stack1)
