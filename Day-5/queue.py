class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        if item is not None:
            self.items.append(item)

    def dequeue(self):
        if len(self.items) > 0:
            item = self.items[0]
            del self.items [0]
            return item
        else: 
            return None 

queue = Queue()
queue.enqueue(10)
queue.enqueue(12)
queue.enqueue(45)

print(queue.items)
print(queue.dequeue())
print(queue.dequeue())
print(queue.dequeue())
print(queue.dequeue())
print(queue.dequeue())