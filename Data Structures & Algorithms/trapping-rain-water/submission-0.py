class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        area = 0
        prefix = [0] * n
        suffix = [0] * n
        prefix_max, suffix_max = 0, 0
        for i in range(n):
            prefix_max = max(prefix_max, height[i])
            prefix[i] = prefix_max
        for i in range(n - 1, -1, -1):
            suffix_max = max(suffix_max, height[i])
            suffix[i] = suffix_max
        for i in range(n):
            curr_area = min(prefix[i], suffix[i]) - height[i]
            if curr_area > 0:
                area += curr_area
        return area



