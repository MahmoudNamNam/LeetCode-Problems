from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # Check if the list is empty or has only one node
        # A list with 0 or 1 nodes cannot have a cycle
        if not head or not head.next:
            return False
        
        # Initialize two pointers:
        # - slow: moves one step at a time
        # - fast: moves two steps at a time
        slow = head
        fast = head.next

        
        # Traverse the linked list
        while fast and fast.next:
            # If slow and fast meet at the same node, there's a cycle
            if slow == fast:
                return True
            
            # Move slow pointer one step forward
            slow = slow.next
            # Move fast pointer two steps forward
            fast = fast.next.next
        
        # If we exit the loop, fast reached the end, meaning no cycle exists
        return False

""""
Let's walk through an example to see how the algorithm works.

Example Linked List:

Consider a linked list with the following nodes:

```
1 -> 2 -> 3 -> 4 -> 5
           ^        |
           |________|
```

Here, the `next` pointer of the last node (5) points back to the node with value 3, creating a cycle.

Step-by-Step Execution:

1. Initialization:
   - `slow` starts at the head (node 1).
   - `fast` starts at the second node (node 2).

   ```
   slow -> 1
   fast -> 2
   ```

2. First Iteration:
   - `slow` moves one step to node 2.
   - `fast` moves two steps to node 4.

   ```
   slow -> 2
   fast -> 4
   ```

3. Second Iteration:
   - `slow` moves one step to node 3.
   - `fast` moves two steps, but because of the cycle, it moves from node 4 to node 5, and then back to node 3.

   ```
   slow -> 3
   fast -> 3
   ```

4. Cycle Detected:
   - At this point, `slow` and `fast` both point to node 3. Since they meet at the same node, the algorithm detects a cycle and returns `True`.

How It Works:

- Cycle Presence:
  - In a linked list with a cycle, the `fast` pointer, moving at twice the speed of the `slow` pointer, will eventually lap the `slow` pointer and meet it again if there's a loop. This is similar to how a faster runner on a circular track will eventually catch up to a slower runner.

- No Cycle:
  - If there were no cycle, the `fast` pointer would eventually reach the end of the list (`None`). The loop would exit, and the function would return `False`.

Example Without a Cycle:

Consider a linked list without a cycle:

```
1 -> 2 -> 3 -> 4 -> 5 -> None
```

- Initialization:
  - `slow` starts at node 1.
  - `fast` starts at node 2.

- Iterations:
  - `slow` and `fast` move through the list, with `slow` always one step behind `fast`.

- Termination:
  - `fast` eventually reaches the end (`None`), and the function returns `False`, indicating there's no cycle.

Summary:

- The algorithm efficiently detects a cycle by using two pointers moving at different speeds.
- If a cycle exists, the two pointers will eventually meet.
- If there's no cycle, the `fast` pointer will reach the end of the list.

"""


