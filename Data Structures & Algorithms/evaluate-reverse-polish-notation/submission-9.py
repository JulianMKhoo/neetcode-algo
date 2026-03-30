class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        if len(tokens) == 1:
            return int(tokens[0])
        if len(tokens) == 0:
            return 0
        n = len(tokens)
        ops = ["+", "-", "*", "/"]
        nums = []
        p = 0

        while p < n:
            if tokens[p] not in ops:
                nums.append(tokens[p])
                p += 1
                continue
            while len(nums) > 0 and p < n:
                if tokens[p] not in ops:
                    nums.append(tokens[p])
                    p += 1
                    continue
                num = int(nums.pop())
                first_num = int(nums.pop())
                if tokens[p] == "+":
                    nums.append(first_num + num)
                elif tokens[p] == "-":
                    nums.append(first_num - num)
                elif tokens[p] == "*":
                    nums.append(first_num * num)
                elif tokens[p] == "/":
                    nums.append(int(first_num / num))
                p += 1
        return nums.pop()






