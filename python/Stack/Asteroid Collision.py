class Solution(object):
    def asteroidCollision(self, asteroids):
        stack = []
        
        for asteroid in asteroids:
            while stack and asteroid < 0 < stack[-1]:
                # A collision occurs when an asteroid is moving left (negative value)
                # and the top of the stack is a right-moving asteroid (positive value).
                
                if stack[-1] < -asteroid:
                    # The top asteroid on the stack is smaller, it gets destroyed (popped)
                    stack.pop()
                    # Continue checking for more possible collisions with the new top
                    continue
                elif stack[-1] == -asteroid:
                    # Both asteroids are of equal size, both get destroyed
                    stack.pop()
                # If the current asteroid is smaller or equal, we break out of the while loop.
                break
            else:
                # If there's no collision or the stack is empty, add the asteroid to the stack
                stack.append(asteroid)
        
        return stack


sol = Solution()
print(sol.asteroidCollision([10, 2, -5, 3, -2, -10, 4, 7]))
print(sol.asteroidCollision([5,10,-5]))