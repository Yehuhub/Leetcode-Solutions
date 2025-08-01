from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
    
        def check(root):
            if not root:
                return 0

            # check if left subtree is unbalanced
            left = check(root.left)
            if left == -1:
                return -1
            
            # check if right subtree is unbalanced
            right = check(root.right)
            if right == -1:
                return -1

            # check if current node is unbalanced
            if abs(right - left) > 1:
                return -1
            
            # return the depth of current node
            return max(left, right) + 1
            
        # check if root is unbalanced
        return check(root) != -1