import random


class RandomQueue:

    def __init__(self):
        self.items = []

    def __str__(self):
        return str(self.items)

    def insert(self, item):
        self.items.append(item)

    def remove(self):   # zwraca losowy element
        rand_idx = random.randrange(len(self.items))
        self.items[rand_idx], self.items[-1] = self.items[-1], self.items[rand_idx]
        return self.items.pop()

    def is_empty(self):
        return not self.items

    def is_full(self):
        return False

    def clear(self):     # czyszczenie listy
        self.items.clear()


randQ = RandomQueue()
print("is Empty? :")
print(randQ.is_empty())
randQ.insert(1)
randQ.insert(2)
randQ.insert(3)
randQ.insert(4)
randQ.insert(5)
print(randQ)
print("is Full? :")
print(randQ.is_full())
randQ.remove()
print(randQ)
randQ.remove()
print(randQ)
randQ.remove()
print(randQ)


randQ.clear()
print(randQ)
