# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        queue=deque([root])
        answer=[]
        if not root:
            return []
        while queue:
            level_size=len(queue)
            ans=[]
            for i in range(level_size):
                node=queue.popleft()
                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)
                ans.append(node.val)
            answer.append(ans)
        return answer


        