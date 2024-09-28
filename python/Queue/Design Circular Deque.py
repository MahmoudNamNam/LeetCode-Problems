class MyCircularDeque:

    def __init__(self, k: int):
        """Initialize the deque with a fixed size k."""
        self.deque = [None] * k  # Create a list of size k
        self.front = 0           # Pointer to the front
        self.rear = 0            # Pointer to the rear
        self.size = 0            # Current number of elements
        self.capacity = k        # Maximum capacity of the deque

    def insertFront(self, value: int) -> bool:
        """Insert an element at the front of the deque. Return True if successful."""
        if self.isFull():
            return False
        self.front = (self.front - 1) % self.capacity  # Move front pointer back in a circular manner
        self.deque[self.front] = value
        self.size += 1
        return True

    def insertLast(self, value: int) -> bool:
        """Insert an element at the rear of the deque. Return True if successful."""
        if self.isFull():
            return False
        self.deque[self.rear] = value
        self.rear = (self.rear + 1) % self.capacity  # Move rear pointer forward in a circular manner
        self.size += 1
        return True

    def deleteFront(self) -> bool:
        """Delete an element from the front of the deque. Return True if successful."""
        if self.isEmpty():
            return False
        self.deque[self.front] = None
        self.front = (self.front + 1) % self.capacity  # Move front pointer forward in a circular manner
        self.size -= 1
        return True

    def deleteLast(self) -> bool:
        """Delete an element from the rear of the deque. Return True if successful."""
        if self.isEmpty():
            return False
        self.rear = (self.rear - 1 + self.capacity) % self.capacity  # Move rear pointer back in a circular manner
        self.deque[self.rear] = None
        self.size -= 1
        return True

    def getFront(self) -> int:
        """Return the element at the front of the deque. If empty, return -1."""
        if self.isEmpty():
            return -1
        return self.deque[self.front]

    def getRear(self) -> int:
        """Return the element at the rear of the deque. If empty, return -1."""
        if self.isEmpty():
            return -1
        return self.deque[(self.rear - 1 + self.capacity) % self.capacity]  # Get the last element in the deque

    def isEmpty(self) -> bool:
        """Check if the deque is empty."""
        return self.size == 0

    def isFull(self) -> bool:
        """Check if the deque is full."""
        return self.size == self.capacity




def run_tests():
    # Test 1: Basic functionality of insertFront and insertLast
    dq = MyCircularDeque(3)
    assert dq.insertLast(1) == True   # [1]
    assert dq.insertLast(2) == True   # [1, 2]
    assert dq.insertFront(3) == True  # [3, 1, 2]
    assert dq.insertFront(4) == False  # Should fail, deque is full
    assert dq.getFront() == 3
    assert dq.getRear() == 2
    
    # Test 2: Deleting from front and rear
    assert dq.deleteLast() == True    # [3, 1]
    assert dq.getRear() == 1
    assert dq.deleteFront() == True   # [1]
    assert dq.getFront() == 1
    assert dq.deleteFront() == True   # []
    assert dq.getFront() == -1        # Empty deque
    assert dq.deleteFront() == False  # Should fail, already empty

    # Test 3: Empty and Full checks
    dq = MyCircularDeque(2)
    assert dq.isEmpty() == True       # Deque should be empty
    assert dq.insertLast(5) == True   # [5]
    assert dq.isEmpty() == False      # Deque should not be empty
    assert dq.insertFront(6) == True  # [6, 5]
    assert dq.isFull() == True        # Deque should be full
    assert dq.insertLast(7) == False  # Should fail, deque is full
    assert dq.deleteLast() == True    # [6]
    assert dq.isFull() == False       # Not full after deletion
    assert dq.deleteFront() == True   # []
    assert dq.isEmpty() == True       # Empty after deletion

    # Test 4: Circular functionality
    dq = MyCircularDeque(3)
    assert dq.insertLast(10) == True  # [10]
    assert dq.insertLast(11) == True  # [10, 11]
    assert dq.insertFront(12) == True  # [12, 10, 11]
    assert dq.isFull() == True        # Deque should be full
    assert dq.getFront() == 12        # Check front
    assert dq.getRear() == 11         # Check rear
    assert dq.deleteFront() == True   # [10, 11]
    assert dq.insertLast(13) == True  # [10, 11, 13]
    assert dq.getRear() == 13         # Rear should be 13

    # Test 5: Alternating operations
    dq = MyCircularDeque(4)
    assert dq.insertFront(1) == True  # [1]
    assert dq.insertLast(2) == True   # [1, 2]
    assert dq.insertFront(3) == True  # [3, 1, 2]
    assert dq.insertLast(4) == True   # [3, 1, 2, 4]
    assert dq.getFront() == 3
    assert dq.getRear() == 4
    assert dq.deleteFront() == True   # [1, 2, 4]
    assert dq.deleteLast() == True    # [1, 2]
    assert dq.getFront() == 1
    assert dq.getRear() == 2

    print("All test cases passed!")


# Run the tests
run_tests()
