from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# use in order traversal to count values in order until you find the kth
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
    
        counter = 0
        result = float("inf")
        
        def find(root):
            nonlocal counter
            if not root:
                return 

            find(root.left)

            counter += 1
            if counter == k:
                nonlocal result
                result = root.val

            find(root.right)

        find(root)
        return result
    

# same solution but using class member to store values
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.counter = 0
        self.k = k
        self.find(root)
        return self.result

    def find(self, root):
        if not root:
            return 

        self.find(root.left)

        self.counter += 1
        if self.counter == self.k:
            self.result = root.val
            return

        self.find(root.right)