# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: TreeNode | None) -> list[int]:
        if not root:
            return []
        d=deque([root])
        answer=[]
        while d:
            level=len(d)
            for i in range(level):
                node=d.popleft()
                if i==level-1:
                    answer.append(node.val)
                if node.left : d.append(node.left)
                if node.right : d.append(node.right)
        return answer
            
