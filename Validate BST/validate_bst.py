from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def check(root, ceiling = float("inf"), floor = float("-inf")):
            # we reached the bottom of the tree and havent failed so it is a BST
            if not root: return True 

            if floor < root.val < ceiling:
                return check(root.left, root.val, floor) and check(root.right, ceiling, root.val)
            # if its not then it isnt a bst
            return False
        
        return check(root)