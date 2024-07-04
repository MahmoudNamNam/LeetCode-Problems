import random

class RandomizedSet:

    def __init__(self):
        self.data = []
        self.index_map = {}

    def insert(self, val: int) -> bool:
        if val in self.index_map:
            return False
        self.data.append(val)
        self.index_map[val] = len(self.data) - 1
        return True

    def remove(self, val: int) -> bool:
        if val not in self.index_map:
            return False
        last_element = self.data[-1]
        idx = self.index_map[val]
        self.data[idx] = last_element
        self.index_map[last_element] = idx
        self.data.pop()
        del self.index_map[val]
        return True

    def getRandom(self) -> int:
        return random.choice(self.data)

# Example usage:
randomizedSet = RandomizedSet()
print(randomizedSet.insert(1))    # Output: True
print(randomizedSet.remove(2))    # Output: False
print(randomizedSet.insert(2))    # Output: True
print(randomizedSet.getRandom())  # Output: 1 or 2
print(randomizedSet.remove(1))    # Output: True
print(randomizedSet.insert(2))    # Output: False
print(randomizedSet.getRandom())  # Output: 2
