from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        #find the depth of each right and left
        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)

        # return the max of right and left as we are in the parent node
        return max(left, right) + 1