class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        memo = {}
        result = []
        bucket = [[] for _ in range(n + 1)]

        for i in nums:
            if i not in memo:
                memo[i] = 1
            else:
                memo[i] += 1

        for keys,v in memo.items():
            bucket[v].append(keys)

        for i in range(len(bucket) - 1, 0,-1):
            for num in bucket[i]:
                result.append(num)
                if len(result) == k:
                    return result
            
        return result