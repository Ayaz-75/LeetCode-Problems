class Solution:
    def maxArea(self, verticalLines: List[int]) -> int:
        maxWater = 0  
        rightPointer = len(verticalLines) - 1  
        leftPointer = 0  
        
        while leftPointer != rightPointer:
            if verticalLines[rightPointer] > verticalLines[leftPointer]:
                currentArea = verticalLines[leftPointer] * (rightPointer - leftPointer)
                leftPointer += 1  
            else:
                currentArea = verticalLines[rightPointer] * (rightPointer - leftPointer)
                rightPointer -= 1  
            
            
            maxWater = max(maxWater, currentArea)
        
        return maxWater