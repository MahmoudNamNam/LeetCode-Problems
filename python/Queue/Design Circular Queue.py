class MyCircularQueue:

    def __init__(self, k: int):
        """Initialize the queue with a given size k."""
        self.queue = [0] * k  # A fixed-size list to hold the elements of the queue
        self.head = -1  # Points to the front of the queue
        self.tail = -1  # Points to the end of the queue
        self.size = k  # Maximum size of the queue
        self.count = 0  # Current number of elements in the queue

    def enQueue(self, value: int) -> bool:
        """Insert an element into the circular queue."""
        if self.isFull():
            return False
        if self.isEmpty():
            self.head = 0
        self.tail = (self.tail + 1) % self.size  # Circular increment
        self.queue[self.tail] = value
        self.count += 1
        return True

    def deQueue(self) -> bool:
        """Delete an element from the circular queue."""
        if self.isEmpty():
            return False
        if self.head == self.tail:  # If there is only one element in the queue
            self.head = -1
            self.tail = -1
        else:
            self.head = (self.head + 1) % self.size  # Circular increment
        self.count -= 1
        return True

    def Front(self) -> int:
        """Get the front item from the queue."""
        if self.isEmpty():
            return -1
        return self.queue[self.head]

    def Rear(self) -> int:
        """Get the last item from the queue."""
        if self.isEmpty():
            return -1
        return self.queue[self.tail]

    def isEmpty(self) -> bool:
        """Checks whether the circular queue is empty or not."""
        return self.count == 0

    def isFull(self) -> bool:
        """Checks whether the circular queue is full or not."""
        return self.count == self.size
myCircularQueue = MyCircularQueue(3)
print(myCircularQueue.enQueue(1))  # True
print(myCircularQueue.enQueue(2))  # True
print(myCircularQueue.enQueue(3))  # True
print(myCircularQueue.enQueue(4))  # False (Queue is full)
print(myCircularQueue.Rear())      # 3
print(myCircularQueue.isFull())    # True
print(myCircularQueue.deQueue())   # True
print(myCircularQueue.enQueue(4))  # True
print(myCircularQueue.Rear())      # 4
