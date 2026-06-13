class Solution:
    def rob(self, nums: List[int]) -> int:
        n=len(nums)
        best=[0]*n
        if n==1 :return nums[0]
        prev1=nums[0]
        prev2=max(nums[0],nums[1])
        for i in range(2,n):
            prev1,prev2=prev2,max(prev2,nums[i]+prev1)
        return prev2
        

        