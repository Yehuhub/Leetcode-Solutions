
# my solution, we basically always want the max node
class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        def dfs(root, max_val):
            if not root:
                return 0
            
            if root.val >= max_val:
                return 1 + dfs(root.left, root.val) + dfs(root.right, root.val)
            else:
                return dfs(root.left, max_val) + dfs(root.right, max_val)
        return dfs(root, root.val)


# this is a slightly cleaner implementation of the same idea
class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        def dfs(root, max_val):
            if not root:
                return 0
            
            res = 1 if root.val >= max_val else 0
            new_max = max(root.val, max_val)
            res += dfs(root.left, new_max)
            res += dfs(root.right, new_max)
            return res
        return dfs(root, root.val)
        