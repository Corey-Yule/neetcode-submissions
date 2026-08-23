class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left, right = 0, len(heights) - 1
        res = 0

        # Iterate while left pointer is less than right
        while left < right:
            area = min(heights[left], heights[right]) * (right-left)
            res = max(res,area)
            # Check if the sum matches the target
            if heights[left] <= heights[right]:
                left += 1
            else:
                right -= 1
        return res
            