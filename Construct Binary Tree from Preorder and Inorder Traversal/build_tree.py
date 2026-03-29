
# this is the solution basically the idea is that the first node in preorder is the actual root,
# then we can get all the elements on the left subtree by finding its index.

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None

        root = TreeNode(preorder[0])
        mid = inorder.index(preorder[0])
        root.left = self.buildTree(preorder[1:mid + 1], inorder[:mid])
        root.right = self.buildTree(preorder[mid + 1 :], inorder[mid + 1:])
        return root



# optimized solution, we use a hashmap to store inorder indices
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        in_map = {val: i for i,val in enumerate(inorder)}

        self.pre_index = 0
        def dfs(l, r):
            if l > r:
                return None


            root_val = preorder[self.pre_index]
            self.pre_index += 1
            root = TreeNode(root_val)
            mid = in_map[root_val]
            root.left = dfs(l, mid - 1)
            root.right = dfs(mid + 1, r)
            return root

        return dfs(0, len(preorder) - 1)
