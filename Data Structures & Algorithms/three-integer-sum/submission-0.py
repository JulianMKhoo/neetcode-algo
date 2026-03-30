class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        result = []
        nums = sorted(nums)
        print(nums)
        for i in range(n - 2):
            j = i + 1
            k = n - 1
            if nums[i] > 0:
                break
            if i > 0 and nums[i - 1] == nums[i]:
                continue
            target = -nums[i]
            while j < k:
                if nums[j] + nums[k] > target:
                    k -= 1
                    continue
                if nums[j] + nums[k] < target:
                    j += 1
                    continue
                result.append([nums[i], nums[j], nums[k]])
                while j < k and nums[j] == nums[j + 1]:
                    j += 1
                while j < k and nums[k] == nums[k - 1]:
                    k -= 1
                j += 1
                k -= 1
        return result

