
# seems complicated at first but actually not that once you get the idea behind it.
# basically we use bin search to find the partition which gives us the correct median
# the way we do it is take the two arrays and always ask if the first array's last element is smaller equal
# to the first element after the partition in the second array and same for the second.
# this gives us a partition of the two arrays that contains half the elements of both arrays
# then all we need to do is get the median
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = nums1, nums2
        total = len(A) + len(B)
        half = total // 2

        if len(B) < len(A):
            A, B = B, A

        l, r= 0, len(A) - 1
        while True:
            i = (l + r) // 2
            j = half - i - 2

            Aleft = A[i] if i >= 0 else float("-inf")
            Aright = A[i+1] if i + 1 < len(A) else float("inf")
            Bleft = B[j] if j >= 0 else float("-inf")
            Bright = B[j+1] if j + 1 < len(B) else float("inf")

            # check if partitioned correctly
            if Aleft <= Bright and Bleft <= Aright:
                # check if need median of odd or even amount of numbers
                if total % 2 == 1:
                    return min(Aright, Bright)
                else:
                    return (max(Aleft, Bleft) + min(Aright, Bright)) / 2
            if Aleft > Bright:
                r = i - 1
            else:
                l = i + 1