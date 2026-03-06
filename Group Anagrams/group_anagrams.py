
# the main idea is that because anagrams are not sensitive to letter order, and since we dont need to compare
# a string with other strings, what we can do is create some sort of key for each string, this key is basically 
# a counter of each letter, it is then converted into a tuple to be a key in the dict.
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mapping = defaultdict(list)

        for word in strs:
            count_map = [0] * 26
            for l in word:
                count_map[ord(l) - 97] += 1
            
            mapping[tuple(count_map)].append(word)

        return list(mapping.values())


