class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # Sort intervals by the start time
        intervals.sort(key=lambda x: x[0])
        merged = []
        for interval in intervals:
            # If merged is empty or there is no overlap, add the interval
            if not merged or merged[-1][1] < interval[0]:
                merged.append(interval)
            else:
                # Overlap detected, merge the intervals
                merged[-1][1] = max(merged[-1][1], interval[1])
        return merged