
# in this problem we always want to replace the letters that are not with max frequency in the substring.
# therefore we take the length of the substring, remove the most frequent size and check if its <= k
# if it is then it means we can replace all other than the most frequent letter and get the desired string.
# we then save the max of the substring lengths.
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        letter_count = {}
        max_size = 0
        max_freq = 0
        l = 0
        
        for r in range(len(s)):
            letter_count[s[r]] = 1 + letter_count.get(s[r], 0)
            max_freq = max(max_freq, letter_count[s[r]])
            
            while (r - l + 1) - max_freq > k:
                letter_count[s[l]] -= 1
                l += 1
            max_size = max(max_size, r - l + 1)

        return max_size