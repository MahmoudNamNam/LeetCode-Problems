from threading import Thread, Lock, Condition

class ZeroEvenOdd:
    def __init__(self, n):
        self.n = n
        self.current_number = 1
        self.zero_turn = True
        self.lock = Lock()
        self.condition = Condition(self.lock)

    def zero(self, printNumber):
        for _ in range(self.n):
            with self.condition:
                while not self.zero_turn:
                    self.condition.wait()
                printNumber(0)
                self.zero_turn = False
                self.condition.notify_all()

    def even(self, printNumber):
        for i in range(2, self.n + 1, 2):
            with self.condition:
                while self.zero_turn or self.current_number % 2 != 0:
                    self.condition.wait()
                printNumber(i)
                self.current_number += 1
                self.zero_turn = True
                self.condition.notify_all()

    def odd(self, printNumber):
        for i in range(1, self.n + 1, 2):
            with self.condition:
                while self.zero_turn or self.current_number % 2 == 0:
                    self.condition.wait()
                printNumber(i)
                self.current_number += 1
                self.zero_turn = True
                self.condition.notify_all()

# Example usage:
def printNumber(x):
    print(x, end='')

n = 5
zero_even_odd = ZeroEvenOdd(n)

# Create threads
thread_zero = Thread(target=zero_even_odd.zero, args=(printNumber,))
thread_even = Thread(target=zero_even_odd.even, args=(printNumber,))
thread_odd = Thread(target=zero_even_odd.odd, args=(printNumber,))

# Start threads
thread_zero.start()
thread_even.start()
thread_odd.start()

# Join threads
thread_zero.join()
thread_even.join()
thread_odd.join()
