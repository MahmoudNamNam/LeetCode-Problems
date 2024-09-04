from typing import List


class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        # Directions: North, East, South, West
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        direction_idx = 0  # Starts facing North
        
        # Convert obstacle list to a set for O(1) look-up
        obstacle_set = set(map(tuple, obstacles))
        
        x,y=0,0
        max_distance =0
        for command in commands:
            if command == -2:
                direction_idx = (direction_idx -1 )%4  # Turn left
            elif command == -1:
                direction_idx = (direction_idx +1 )%4  # Turn right
            else:
                for _ in range(command):
                    new_x= x + directions[direction_idx][0]
                    new_y= y + directions[direction_idx][1]
                    # Check if the new position is an obstacle
                    if (new_x,new_y) not in obstacle_set:
                        x,y=new_x,new_y
                        max_distance = max(max_distance, x*x + y*y)
        return max_distance

sol = Solution()

print(sol)