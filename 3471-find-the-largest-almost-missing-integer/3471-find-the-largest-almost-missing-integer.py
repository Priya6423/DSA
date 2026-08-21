class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:
        n=len(nums)
        if n==k:
            return max(nums)
        has={}
        for i in range(n):
            if nums[i] in has:
                has[nums[i]]+=1
            else:
                has[nums[i]]=1
        if k==1:
            return max((x for x in nums if has[x]==1),default=-1)
        first=nums[0] if has[nums[0]]==1 else -1
        last=nums[-1] if has[nums[-1]]==1 else -1
        return max(first,last)