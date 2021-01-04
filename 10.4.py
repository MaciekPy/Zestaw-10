class Queue:

    def __init__(self):
        self.items = []

    def __str__(self):  # podglądanie kolejki
        return str(self.items)

    def is_empty(self):
        return not self.items

    def is_full(self):  # nigdy nie jest pusta
        return False

    def put(self, data):
        if self.is_full():
            raise OverflowError("Brak miejsca w kolejce.")
        self.items.append(data)

    def get(self):
        if self.is_empty():
            raise ValueError("Brak elementów w kolejce.")
        return self.items.pop(0)  # mało wydajne!


que = Queue()
print("is Empty? :")
print(que.is_empty())
que.put(1)
que.put(2)
que.put(3)
que.put(4)
que.put(5)
print(que)
print("is Full? :")
print(que.is_full())
que.get()
print(que)
que.get()
print(que)
que.get()
print(que)
