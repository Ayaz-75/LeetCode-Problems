import math
from typing import List

class Solution:
    def validSquare(self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:
        def distance_sq(p1, p2):
            return (p2[0] - p1[0]) ** 2 + (p2[1] - p1[1]) ** 2
        
        # Calculate all six distances squared
        dists = [
            distance_sq(p1, p2),
            distance_sq(p1, p3),
            distance_sq(p1, p4),
            distance_sq(p2, p3),
            distance_sq(p2, p4),
            distance_sq(p3, p4)
        ]
        
        # Use a set to find the unique distances
        dist_set = set(dists)
        
        # A valid square should only have 2 unique distances (sides and diagonals)
        if len(dist_set) != 2:
            return False
        
        # The side length should appear 4 times and the diagonal length should appear 2 times
        side_length = min(dist_set)
        diagonal_length = max(dist_set)
        
        if dists.count(side_length) == 4 and dists.count(diagonal_length) == 2:
            return True
        
        return False

# Example usage:
# sol = Solution()
# print(sol.validSquare([0,0], [1,1], [1,0], [0,1]))  # True
# print(sol.validSquare([0,0], [1,1], [1,0], [0,2]))  # False
