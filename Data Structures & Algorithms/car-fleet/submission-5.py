class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted(zip(position, speed), reverse=True)
        stack = []

        for i in range(len(cars)):
            pos, spd = cars[i]
            time = (target - pos) / spd

            if i == 0 or time > stack[-1]:
                stack.append(time)
            else:
                continue
                   
        return len(stack)

        