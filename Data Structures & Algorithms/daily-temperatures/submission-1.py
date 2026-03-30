class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        result = [0] * n
        indices = [0]
        for i in range(1, n):
            curr_temp = temperatures[i]
            if curr_temp < temperatures[indices[len(indices) - 1]]:
                indices.append(i)
            else:
                while len(indices) > 0:
                    prev_days = indices.pop()
                    if temperatures[prev_days] >= curr_temp:
                        indices.append(prev_days)
                        break
                    result[prev_days] = i - prev_days
                indices.append(i)
        return result

