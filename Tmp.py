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
    
    

# 103. Binary Tree Zigzag Level Order Traversal
    
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        queue = deque()
        queue.append(root)
        result = []
        right = False

        while queue:
            tmp = []
            for idx in range(len(queue)):
                curr = queue.popleft()
                if curr:
                    tmp.insert(0 if right else len(tmp), curr.val)
                    if curr.left:
                        queue.append(curr.left)
                    if curr.right:
                        queue.append(curr.right)
            right = not right
            if tmp:
                result.append(tmp)
        
        return result

# 35. Search Insert Position 
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        low, high = 0, len(nums) - 1
        while low <= high:
            mid = (low + high) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                high = mid - 1
            else:
                low = mid + 1
        return low

    ...
