class PriorityQueue:

    # Constructor    
    def __init__(self):
        self.queue = []

    # Check if the queue is empty
    def is_empty(self):
        return len(self.queue) == 0

    # Enqueue an item with a priority
    def enqueue(self, item, priority):
        self.queue.append((item, priority))
        self.queue.sort(key=lambda x: x[1])

    # Dequeue an item
    def dequeue(self):
        if self.is_empty():
            return None
        return self.queue.pop(0)[0]

    # Peek at the first item
    def peek(self):
        if self.is_empty():
            return None
        return self.queue[0][0]

    # Get the size of the queue
    def size(self):
        return len(self.queue)