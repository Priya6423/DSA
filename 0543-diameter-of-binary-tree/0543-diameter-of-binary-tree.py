# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        diameter=[0]
        def helper(root):
            if not root:
                return 0
            else:
                left=helper(root.left)
                right=helper(root.right)
                diameter[0]=max(left+right,diameter[0])
            return 1+max(left,right)
        helper(root)
        return diameter[0]
        