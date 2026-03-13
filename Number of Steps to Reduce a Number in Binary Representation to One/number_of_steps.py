
# this is my solution it works and does as required but is stricly pythonic and is not manipulating bits
class Solution:
    def numSteps(self, s: str) -> int:
        s = int(s, 2)
        count = 0

        while s != 1:
            if s % 2 == 0:
                s >>= 1
            else:
                s += 1
            count += 1

        return count
    

class Solution:
    def numSteps(self, s: str) -> int:
        carry = 0
        count = 0

        for i in range(len(s), 0, -1):
            bit = (int(s[i]) + carry) % 2

            if bit == 1:
                carry= 1
                steps +=2
            else:
                steps += 1

        return steps + carry