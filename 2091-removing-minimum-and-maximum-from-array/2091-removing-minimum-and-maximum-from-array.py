class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        mini=0
        maxi=0
        for i in range(len(nums)):
            if nums[i]>nums[maxi]:
                maxi=i
            elif nums[i]<nums[mini]:
                mini=i
        left=min(mini,maxi)
        right=max(mini,maxi)
        mini1=min(right+1,len(nums) - left)
        mini2=min((left + 1) + (len(nums) - right),mini1)
        return mini2