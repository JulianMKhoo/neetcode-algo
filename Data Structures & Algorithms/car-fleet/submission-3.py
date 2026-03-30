class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        n = len(position)
        sort_arr = sorted(zip(position, speed), reverse=True)
        mono = []
        for i in range(n):
            curr_position = sort_arr[i][0]
            curr_speed = sort_arr[i][1]
            curr_time = (target - curr_position) / curr_speed
            if len(mono) <= 0:
                mono.append(curr_time)
                continue
            mono.append(curr_time)
            if len(mono) > 1 and mono[-1] <= mono[-2]:
                mono.pop()
        return len(mono)





