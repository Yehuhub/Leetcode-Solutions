
# this is the solution I came up with, basically we run a fixed size sliding window
# we basically on each slide of the window update the letter count according to the letter we got to,
# so on each iteration we remove the old left and add the new right
# then we compare the arrays.
# since arrays are size 26 we get O(n) complexity
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        s1_count = [0] * 26
        s2_count = [0] * 26

        for char in s1:
            s1_count[ord(char) - ord('a')] += 1

        for i in range(len(s1)):
            s2_count[ord(s2[i]) - ord('a')] += 1


        l = 0
        for r in range(len(s1), len(s2)):
            if s1_count == s2_count:
                return True
            s2_count[ord(s2[r]) - ord('a')] += 1
            s2_count[ord(s2[l]) - ord('a')] -= 1
            l += 1
        return s1_count == s2_count
        
# this is an optimized solution which is very similar,
# basically instead of comparing the entire arrays we check for matches,
# if we add the new right count we check if the index which we added to is now the same in the other array
# if it does it means we got a match, same goes for the opposite in the left.
# now when we get 26 matches it means that all 26 indices are matching in both arrays, which means we found
# a permutation
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        s1Count, s2Count = [0] * 26, [0] * 26
        for i in range(len(s1)):
            s1Count[ord(s1[i]) - ord('a')] += 1
            s2Count[ord(s2[i]) - ord('a')] += 1

        matches = 0
        for i in range(26):
            matches += (1 if s1Count[i] == s2Count[i] else 0)

        l = 0
        for r in range(len(s1), len(s2)):
            if matches == 26:
                return True

            index = ord(s2[r]) - ord('a')
            s2Count[index] += 1
            if s1Count[index] == s2Count[index]:
                matches += 1
            elif s1Count[index] + 1 == s2Count[index]:
                matches -= 1

            index = ord(s2[l]) - ord('a')
            s2Count[index] -= 1
            if s1Count[index] == s2Count[index]:
                matches += 1
            elif s1Count[index] - 1 == s2Count[index]:
                matches -= 1
            l += 1
        return matches == 26