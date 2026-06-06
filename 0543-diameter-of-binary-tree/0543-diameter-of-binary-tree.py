# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        depth=0
        def helper(root):
            nonlocal depth
            if not root:
                return 0
            else:
                left=helper(root.left)
                right=helper(root.right)
                depth=max(depth,left+right)
                return 1+max(left,right)
        helper(root)
        return depth