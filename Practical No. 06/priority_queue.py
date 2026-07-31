class PriorityQueue:
    def __init__(self, capacity):
        self.capacity = capacity
        self.queue = []

    def is_empty(self):
        return len(self.queue) == 0

    def is_full(self):
        return len(self.queue) >= self.capacity

    def enqueue(self, item, priority):
        if self.is_full():
            return False

        self.queue.append((item, priority))
        self.queue.sort(key=lambda x: x[1])
        return True

    def dequeue(self):
        if self.is_empty():
            return None

        return self.queue.pop(0)

    def traverse(self):
        return self.queue

    def ascending(self):
        return sorted(self.queue, key=lambda x: x[1])

    def descending(self):
        return sorted(self.queue, key=lambda x: x[1], reverse=True)