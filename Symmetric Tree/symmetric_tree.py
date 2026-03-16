# this is the solution, I wrote it
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
    
        def mirror(left, right):
            if not left and not right:
                return True
            if (right and not left) or (left and not right):
                return False
            return left.val==right.val and mirror(left.left, right.right) and mirror(left.right, right.left)

        return mirror(root.left, root.right)


# slight improvement to the if statement,
# we know that either left or right or both have value so we can just check if not left or not right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
    
        def mirror(left, right):
            if not left and not right:
                return True
            if not left or not right:
                return False
            return left.val==right.val and mirror(left.left, right.right) and mirror(left.right, right.left)

        return mirror(root.left, root.right)
