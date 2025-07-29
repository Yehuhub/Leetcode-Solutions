class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


#this is my naive approach which works but is terribly slow.
#here we find in which side of the tree is p and q.
#after we know that we can determine who is the lowest common ancestor

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        if not root or p == root or q == root:
            return root

        #find on which side of the binary tree are the required nodes
        p_on_left = self.find(root.left, p)

        q_on_left = self.find(root.left, q)

        if p_on_left != q_on_left:
            return root
        elif not p_on_left and not q_on_left:
            return self.lowestCommonAncestor(root.right, p, q)
        else:
            return self.lowestCommonAncestor(root.left, p, q)

    def find(self, root: 'TreeNode', node: 'TreeNode'):
        if not root: return False

        if root == node:
            return True
        
        return self.find(root.left, node) or self.find(root.right, node)



# a better solution that involves only a single iteration of the tree.
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # we either gotten to the bottom of the tree
        # or we found p or q, so we want to return them
        if not root or root == p or root == q: 
            return root
        
        # will keep going into the recursion until we find p/q
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        #left and right meaning, we have one of them on each side
        if left and right:
            return root
        #left means we didnt find anything on the right and only on the left
        elif left:
            return left
        #right means we didnt find anything on the left and only on the right
        elif right:
            return right

