from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.res = 0 #our result

        def getDiameter(root: Optional[TreeNode]):
            if not root: # we reached the end of a branch
                return 0
            
            #find the diamater of each child
            right = getDiameter(root.right)
            left = getDiameter(root.left)

            # we save the max which is either the result or two children combined
            self.res = max(self.res, left+right) 

            #we return 1+either max of left and right to keep calculating
            return 1 + max(left,right)
            
        getDiameter(root)
        return self.res