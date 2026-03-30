class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        memo = {}
        for s in strs:
            t = [0] * 26
            for c in s:
                t[ord(c)-97] += 1
            t = tuple(t)
            if t not in memo:
                memo[t] = [s]
            else:
                memo[t].append(s)
        return [memo[i] for i in memo]