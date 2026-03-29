

# we use bfs for this solution, we have a q of all node at current level and always keep the last
# node in var right, this way the last node from left to right in level is in right, then we add it to res
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        if not root: 
            return res

        q = deque()
        q.append(root)

        while q:
            right = None
            level_size = len(q)
            for _ in range(level_size):
                node = q.popleft()
                if node:
                    right = node
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            res.append(right.val)
        return res
