
# the main idea is that we dont need to check the entire window against the t_counter,
# whenever we reached one of the letters in t we add it to our window and increase its counter, 
# then basically we hold a count of how many more we need, if we have exactly how much we need we 
# can start popping letters from the left until we are not valid this way we can have the current min 
# if we find a smaller one letter it will be the new min
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""
        t_counter, window = {}, {}
        for char in t:
            t_counter[char] = t_counter.get(char, 0) + 1


        need, have = len(t_counter), 0
        res = ""
        res_len = float('inf')
        l = 0
        for r in range(len(s)):
            c = s[r]
            window[c] = 1 + window.get(c, 0)

            if c in t_counter and window[c] == t_counter[c]:
                have += 1

            while have == need:
                if (r - l + 1) < res_len:
                    res_len = r - l + 1
                    res = s[l:r+1]

                window[s[l]] -= 1
                if s[l] in t_counter and window[s[l]] < t_counter[s[l]]:
                    have -= 1
                l += 1
        return res



            