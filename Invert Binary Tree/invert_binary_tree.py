from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root: return root

        # invert each of the children
        left = self.invertTree(root.left)
        right = self.invertTree(root.right)

        # assign left child to be right and right to be left
        root.left = right
        root.right = left

        # return the inverted node
        return root