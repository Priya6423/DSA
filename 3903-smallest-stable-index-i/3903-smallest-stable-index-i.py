class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        n=len(nums)
        suff=[0]*n
        maxi=nums[0]
        mini=nums[n-1]
        for j in range(n-1,-1,-1):
            if nums[j]<mini:
                mini=nums[j]
            suff[j]=mini
        for i in range(n):
            maxi=max(maxi,nums[i])
            if maxi-suff[i]<=k:
                return i
        return -1
            
        