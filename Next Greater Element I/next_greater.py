# brute force solution
# basically we index nums1 to a hashmap
# then we run on nums2 and check if that nums2[i] is in the map, if it isnt it means we dont need to find
# its greater element.
# if it is we check from it onwards for the first one larger than it and we store it in the result
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        n1_indexed = {val : i for i, val in enumerate(nums1)}

        res = [-1] * len(nums1)

        for i in range(len(nums2)):
            if nums2[i] not in n1_indexed:
                continue
            for j in range(i + 1, len(nums2)):
                if nums2[j] > nums2[i]:
                    idx = n1_indexed[nums2[i]]
                    res[idx] = nums2[j]
                    break
        return res

# optimal solution uses a stack, basically we add items to the stack only if they appear in nums1,
# each time we reach a new num on nums2 we pop all items smaller than it on the stack to maintain a decreasing
# stack.
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        n1_indexed = {val : i for i, val in enumerate(nums1)}
        res = [-1] * len(nums1)

        stack = []

        for i in range(len(nums2)):
            curr = nums2[i]

            while stack and stack[-1] < curr:
                val = stack.pop()
                idx = n1_indexed[val]
                res[idx] = curr
            if curr in n1_indexed:
                stack.append(curr)

        return res