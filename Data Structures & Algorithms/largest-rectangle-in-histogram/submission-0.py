class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        heights.append(0)
        n = len(heights)
        mono = [0]
        result = 0
        for i in range(n):
            curr_height = heights[i]
            prev_height = heights[mono[-1]]
            if curr_height >= prev_height:
                mono.append(i)
                continue
            while len(mono) > 0 and heights[mono[-1]] > curr_height:
                height = heights[mono.pop()]
                if len(mono) == 0:
                    left = -1
                else:
                    left = mono[-1]
                right = i
                area = height * (right - left - 1)
                result = max(result, area)
            mono.append(i)

        return result

