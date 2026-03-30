class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        n = len(nums)
        clean = set()
        result = 0
        
        for n in nums:
            clean.add(n)
        
        for n in clean:
            curr = n - 1
            if curr not in clean:
                count = 1
                temp = 1
                while n + count in clean:
                    temp += 1
                    count += 1
                result = max(result, temp)
        return result