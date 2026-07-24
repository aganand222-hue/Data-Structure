class Queue:
    def __init__(self, max_size):
        self.queue = []
        self.max_size = max_size

    def is_empty(self):
        return len(self.queue) == 0

    def is_full(self):
        return len(self.queue) == self.max_size

    def enqueue(self, item):
        if self.is_full():
            return False, "Queue is full."
        self.queue.append(item)
        return True, f"Enqueued: {item}"

    def dequeue(self):
        if self.is_empty():
            return False, "Queue is empty."
        item = self.queue.pop(0)
        return True, f"Dequeued: {item}"

    def peek(self):
        if self.is_empty():
            return False, "Queue is empty."
        return True, self.queue[0]

    def traverse(self):
        return self.queue

    def display_list(self):
        return self.queue
