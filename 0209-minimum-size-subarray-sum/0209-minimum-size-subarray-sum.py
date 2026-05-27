class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left=0
        mini=float('inf')
        sums=0
        for right in range(len(nums)):
            sums+=nums[right]
            while sums>=target:
                mini=min(mini,right-left+1)
                sums-=nums[left]
                left+=1
        return 0 if mini==float('inf') else mini

        