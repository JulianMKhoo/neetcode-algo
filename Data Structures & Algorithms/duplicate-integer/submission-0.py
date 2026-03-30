class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        temps = set()
        for i in nums:
            if i not in temps:
                temps.add(i)
            else:
                return True
        return False