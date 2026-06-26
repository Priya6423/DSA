class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curr=nums[0]
        res=nums[0]
        for num in range(1,len(nums)):
            curr=max(curr+nums[num],nums[num])
            res=max(res,curr)
        return res

        