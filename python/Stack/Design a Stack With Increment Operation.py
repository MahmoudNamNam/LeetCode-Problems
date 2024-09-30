class CustomStack:

    def __init__(self, maxSize: int):
        self.stack=[]
        self.maxSize = maxSize
        self.size=0

    def push(self, x: int) -> None:
        if self.size <self.maxSize:
            self.stack.append(x)
            self.size +=1
        return None

    def pop(self) -> int:
        if self.size > 0:
            self.size -= 1
            return self.stack.pop()
        return -1


    def increment(self, k: int, val: int) -> None:
        k=min(k,self.size)
        for i in range(k):
            self.stack[i] += val
        return None 