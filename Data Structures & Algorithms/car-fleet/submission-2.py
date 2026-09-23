class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
# 1. Pair and sort cars by position in descending order (closest to target first)
        cars = sorted(zip(position, speed), reverse=True)
        
        stack = []
        # 2. Iterate through the sorted cars
        for i in range(len(cars)):
            pos, spd = cars[i]
            time = (target - pos) / spd
            
            # 3. If it's the first car or takes longer than the fleet ahead, it forms a new fleet
            if i == 0 or time > stack[-1]:
                stack.append(time)
            else:
                continue
                
        return len(stack)

        