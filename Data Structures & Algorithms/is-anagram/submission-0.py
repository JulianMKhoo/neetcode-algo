class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        first_temps, second_temps = {}, {}
        for i in s:
            first_temps[i] = first_temps.get(i,0) + 1
        for i in t:
            second_temps[i] = second_temps.get(i,0) + 1
        return first_temps == second_temps
