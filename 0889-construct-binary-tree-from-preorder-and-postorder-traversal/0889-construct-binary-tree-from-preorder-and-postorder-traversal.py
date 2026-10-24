# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructFromPrePost(self, preorder: list[int], postorder: list[int]) -> TreeNode | None:
        if not preorder:
            return None
        if len(preorder)==1:
            root=TreeNode(preorder[0])
            return root
        root=TreeNode(preorder[0])
        k=postorder.index(preorder[1])
        root.left=self.constructFromPrePost(preorder[1:k+2],postorder[:k+1])
        root.right=self.constructFromPrePost(preorder[k+2:],postorder[k+1:-1])
        return root