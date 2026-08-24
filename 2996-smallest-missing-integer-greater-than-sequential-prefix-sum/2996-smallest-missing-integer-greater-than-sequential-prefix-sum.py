class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        num=set(nums)
        cnt=nums[0]
        for i in range(1,len(nums)):
            if nums[i]==nums[i-1]+1:
                cnt+=nums[i]
            else:
                break
        while cnt in num:
            cnt+=1
        return cnt
        