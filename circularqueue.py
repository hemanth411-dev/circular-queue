# circular_queue.py

class CircularQueue:
    def __init__(self, capacity):
        self.capacity = capacity
        self.queue = [None] * capacity  
        self.front = -1  
        self.rear = -1   

    def is_empty(self):
        return self.front == -1

    def is_full(self):
        return (self.rear + 1) % self.capacity == self.front

    def enqueue(self, item):
        if self.is_full():
            print("Queue is at full capacity! Cannot enqueue.")
            return
        
        if self.is_empty():
            self.front = 0  
        self.rear = (self.rear + 1) % self.capacity 
        self.queue[self.rear] = item 

    def dequeue(self):
        if self.is_empty():
            print("Queue is empty, cannot dequeue!")
            return None

        item = self.queue[self.front]
        if self.front == self.rear:  
            self.front = self.rear = -1
        else:
            self.front = (self.front + 1) % self.capacity 
        return item

    def peek_front(self):
        if self.is_empty():
            print("Queue is empty.")
            return None
        return self.queue[self.front]

    def peek_rear(self):
        if self.is_empty():
            print("Queue is empty.")
            return None
        return self.queue[self.rear]

    def display(self):
        if self.is_empty():
            print("Queue is currently empty.")
            return
        
        idx = self.front
        while idx != self.rear:
            print(self.queue[idx], end=" -> ")
            idx = (idx + 1) % self.capacity
        print(self.queue[self.rear])

    def current_size(self):
        if self.is_empty():
            return 0
        elif self.rear >= self.front:
            return self.rear - self.front + 1
        else:
            return self.capacity - self.front + self.rear + 1
