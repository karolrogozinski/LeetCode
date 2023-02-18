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



# 226. Invert Binary Tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def invert(node: Optional[TreeNode]) -> None:
            if node:
                node.left, node.right = node.right, node.left
                invert(node.left)
                invert(node.right)

        invert(root)
        return root
