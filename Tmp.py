# Solution for 783. Minimum Distance Between BST Nodes

Class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        def inorder(node) -> None:
            nonlocal min_diff, prev
            if node:
                inorder(node.left)
                min_diff = min(min_diff, node.val - prev)
                prev = node.val
                inorder(node.right)
        
        min_diff = float(inf)
        prev = float(-inf)
        inorder(root)
        return min_diff
