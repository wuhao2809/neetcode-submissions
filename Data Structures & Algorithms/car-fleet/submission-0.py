class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # [0,1,4,7] [1,2,2,1]
        # [1,3,6,8]
        # time: [10, 4.5, 3, 3]
        # change it to monotonic decreasing stack, count the elements in stack, that's the number
        pos_speed = []
        n = len(position)
        for i, pos in enumerate(position):
            pos_speed.append((pos, speed[i]))
        
        pos_speed.sort()
        time = []
        for i, curr in enumerate(pos_speed):
            curr_time = (target - curr[0])/curr[1]
            while time and time[-1] <= curr_time:
                time.pop()
            time.append(curr_time)
        return len(time)
            
