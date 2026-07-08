class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
            zipped = sorted(zip(position, speed), reverse=True)
            stack = []
            for idx,item in enumerate(zipped):
                time = (target - item[0]) / item[1]
                if idx != 0:
                    if time > stack[-1]:
                        stack.append(time)
                else:
                    stack.append(time)
            return len(stack) 
                    