
# the idea here is that whichever car that start latest, if any car finishes before it then it is in the same fleet
# as it, because it cannot pass it.
# so unless we add a time to the stack that is larger than the last value then we can pop it since it doesnt matter.
# the main thing to remember in the solution is the time is the actual finish time of each car.
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        zipped = list(zip(position, speed))
        zipped.sort(reverse=True)

        stack = []

        for pos, speed in zipped:
            time = (target - pos) / speed
            stack.append(time)
            if len(stack) >= 2 and stack[-2] >= stack[-1]:
                stack.pop()
        return len(stack)
            