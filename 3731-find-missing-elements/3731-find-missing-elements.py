class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        present=set(nums)
        n=min(nums)
        m=max(nums)
        ans=[]
        for i in range(n,m+1):
            if i not in present:
                ans.append(i)
        return ans
       
        