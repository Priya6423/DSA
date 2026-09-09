class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        n=len(nums)
        pref=[0]*n
        suff=[0]*n
        maxi=nums[0]
        mini=nums[n-1]
        for i in range(n):
            if nums[i]>maxi:
                maxi=nums[i]
            pref[i]=maxi
        for j in range(n-1,-1,-1):
            if nums[j]<mini:
                mini=nums[j]
            suff[j]=mini
        for i in range(n):
            if pref[i]-suff[i]<=k:
                return i
        return -1
            
        