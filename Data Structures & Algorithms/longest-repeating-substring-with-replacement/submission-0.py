class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        n = len(s)
        left, right, result, max_f = 0,0,0,0
        memo = {}
        while right < n:
            if s[right] not in memo:
                memo[s[right]] = 1
            else:
                memo[s[right]] += 1
            max_f = max(max_f, memo[s[right]])
            if (right - left + 1) - max_f > k:
                memo[s[left]] -= 1
                left += 1
            else:
                result = max(result, right - left + 1)
            right += 1
        return result