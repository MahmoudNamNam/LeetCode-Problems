class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        pos = [0, 0]
        direction = 0
        
        directions = {
            0: (0, 1),    # North
            90: (1, 0),   # East
            180: (0, -1), # South
            270: (-1, 0)  # West
        }
        
        for ins in instructions:
            if ins == 'R':
                direction = (direction + 90) % 360
            elif ins == 'L':
                direction = (direction - 90) % 360
            elif ins == 'G':
                dx, dy = directions[direction]
                pos[0] += dx
                pos[1] += dy
        
        return pos == [0, 0] or direction != 0

sol = Solution()
instructions = "GGLLGG"
print(sol.isRobotBounded(instructions))  # Output: True
