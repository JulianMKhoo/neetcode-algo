class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n = len(heights)
        area = 0
        left, right = 0, n - 1
        while left < right:
            area = max(area, (right - left) * min(heights[left], heights[right]))
            if heights[left] < heights[right]:
                left += 1
                continue
            if heights[right] < heights[left]:
                right -= 1
                continue
            left += 1
            right -= 1
        return area

