from collections import deque

class RecentCounter:
    def __init__(self):
        self.queue = deque()

    def ping(self, t: int) -> int:
        # Add the new request time to the queue
        self.queue.append(t)
        
        # Remove requests that are older than t - 3000
        while self.queue[0] < t - 3000:
            self.queue.popleft()
        
        # Return the number of requests in the last 3000 ms
        return len(self.queue)
