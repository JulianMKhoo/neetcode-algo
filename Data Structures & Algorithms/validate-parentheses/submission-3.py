class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False
        n = len(s)
        table = {"(": ")", "{": "}", "[": "]"}
        memo = deque()
        p = 0
        while p < n:
            if s[p] in table:
                memo.append(s[p])
                p += 1
            else:
                if len(memo) == 0:
                    return False
                while len(memo) > 0 and p < n:
                    v = memo.pop()
                    if table[v] != s[p]:
                        return False
                    p += 1
        if len(memo) > 0:
            return False
        return True




