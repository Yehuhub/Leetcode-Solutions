
from math import log2
# first solution is a bit clunky but runs well in O(log(n))
# we search if the prime number making it is just 2, if it is than it is true
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        
        if n == 1:
            return True

        if n % 2 == 1 or n <= 0:
            return False
        
        while n > 1:
            n /= 2
            if not n.is_integer():
                return False
            
        return True

# this is a cleaner solution working the same way, it removes the need to check for the type of the number
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        
        if n <= 0:
            return False
        
        while n > 0:
            if n == 1:
                return True
            if n%2 != 0:
                return False
            n //= 2
            
        return False


# this is the cleanest solution it check if log2 of the number is whole, if it is it means the number
# can be made by 2**x
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n <= 0:
            return False

        return log2(n).is_integer()