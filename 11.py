class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left = 0 
        right = len(height)- 1;
        maxArea = 0;
        while (left < right and left >= 0 and right <= len(height) - 1):
            maxArea = max(maxArea, min(height[left], height[right]) * (right - left));
            if (height[left] > height[right]):
                right=right-1;
            else:
                left=left+1;
        return maxArea
sol=Solution()
print sol.maxArea([1, 2, 3, 4])
