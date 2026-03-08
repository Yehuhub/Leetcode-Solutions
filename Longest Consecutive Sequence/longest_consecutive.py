
# we start by creating set becuase it will help us find the starting element of a sequence in O(1).
# then for each of the starting elements we look for all of the next elements.
# this runs in O(n) since the inside loop is only running for starting elements.
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        all_nums = set(nums)
        max_sequence = 0
        
        for num in nums:
            if num - 1 not in all_nums:
                length = 0
                while num + length in all_nums:
                    length += 1
                max_sequence = max(max_sequence, length)

        return max_sequence