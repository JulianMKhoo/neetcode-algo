class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        left, right, result = 0,0,0
        memo = set()
        while left < n and right < n:
            if s[right] in memo:
                memo.remove(s[left])
                left += 1
            else:
                memo.add(s[right])
                right += 1
                result = max(result, right - left)
        return result